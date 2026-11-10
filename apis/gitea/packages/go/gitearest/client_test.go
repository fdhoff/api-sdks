package gitearest_test

import (
	"bytes"
	"context"
	"encoding/base64"
	"errors"
	"fmt"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"strings"
	"sync"
	"testing"
	"time"

	gitea "github.com/fdhoff/api-sdks/apis/gitea/packages/go/gitearest"
)

const (
	token    = "synthetic-access-token-0000000000000000"
	password = "synthetic-password-0000"
	otp      = "730194"
)

type seen struct {
	method, uri string
	header      http.Header
}

type recorder struct {
	lock     sync.Mutex
	requests []seen
}

func (r *recorder) add(request *http.Request) int {
	r.lock.Lock()
	defer r.lock.Unlock()
	r.requests = append(r.requests, seen{request.Method, request.RequestURI, request.Header.Clone()})
	return len(r.requests)
}

func (r *recorder) all() []seen {
	r.lock.Lock()
	defer r.lock.Unlock()
	return append([]seen(nil), r.requests...)
}

// mock serves handler at a fresh origin, recording every request.
func mock(t *testing.T, handler func(w http.ResponseWriter, r *http.Request, count int)) (*httptest.Server, *recorder) {
	t.Helper()
	record := &recorder{}
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		handler(w, r, record.add(r))
	}))
	t.Cleanup(server.Close)
	return server, record
}

func newClient(t *testing.T, baseURL string, credentials gitea.Credentials, options ...gitea.Option) *gitea.Client {
	t.Helper()
	defaults := []gitea.Option{gitea.WithRetryBaseDelay(time.Millisecond), gitea.WithRateLimitWait(time.Millisecond)}
	client, err := gitea.NewClient(baseURL, credentials, append(defaults, options...)...)
	if err != nil {
		t.Fatal(err)
	}
	return client
}

func replyJSON(w http.ResponseWriter, status int, body string) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	fmt.Fprint(w, body)
}

func TestNewClientValidatesItsArguments(t *testing.T) {
	cases := map[string]struct {
		baseURL     string
		credentials gitea.Credentials
		options     []gitea.Option
	}{
		"no base URL":                 {"", gitea.Token(token), nil},
		"a relative URL":              {"gitea.example.com", gitea.Token(token), nil},
		"another scheme":              {"ftp://gitea.example.com", gitea.Token(token), nil},
		"a query":                     {"https://gitea.example.com?a=1", gitea.Token(token), nil},
		"a fragment":                  {"https://gitea.example.com/#top", gitea.Token(token), nil},
		"a user":                      {"https://someone@gitea.example.com", gitea.Token(token), nil},
		"no host":                     {"https:///git", gitea.Token(token), nil},
		"the API path already on":     {"https://gitea.example.com/api/v1", gitea.Token(token), nil},
		"the API path and a slash":    {"https://gitea.example.com/api/v1/", gitea.Token(token), nil},
		"no credentials":              {"https://gitea.example.com", nil, nil},
		"an empty token":              {"https://gitea.example.com", gitea.Token(""), nil},
		"an empty username":           {"https://gitea.example.com", gitea.Basic("", password), nil},
		"an empty password":           {"https://gitea.example.com", gitea.Basic("synthetic-user", ""), nil},
		"an empty one-time password":  {"https://gitea.example.com", gitea.BasicWithOTP("synthetic-user", password, ""), nil},
		"an empty sudo user":          {"https://gitea.example.com", gitea.Token(token), []gitea.Option{gitea.WithSudo("")}},
		"an unparsable URL":           {"https://gitea exa.com", gitea.Token(token), nil},
		"an unparsable URL with path": {"https://gitea.example.com/%zz", gitea.Token(token), nil},
	}
	for name, item := range cases {
		t.Run(name, func(t *testing.T) {
			if _, err := gitea.NewClient(item.baseURL, item.credentials, item.options...); err == nil {
				t.Fatal("expected an error")
			}
		})
	}
}

func TestTheClientAddsTheAPIPathToTheInstanceURL(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{"version":"1.0.0"}`)
	})
	ctx := context.Background()
	for _, root := range []string{server.URL, server.URL + "/", server.URL + "/git", server.URL + "/git/"} {
		version, err := newClient(t, root, gitea.Token(token)).Misc.GetVersion(ctx)
		if err != nil || *version.Version != "1.0.0" {
			t.Fatalf("%s: version is %v, %v", root, version, err)
		}
	}
	paths := []string{}
	for _, request := range record.all() {
		paths = append(paths, request.uri)
	}
	want := "/api/v1/version /api/v1/version /git/api/v1/version /git/api/v1/version"
	if strings.Join(paths, " ") != want {
		t.Fatalf("paths are %v", paths)
	}
}

func TestEachCredentialSendsItsHeaders(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{"id":1,"login":"synthetic-user"}`)
	})
	encoded := base64.StdEncoding.EncodeToString([]byte("synthetic-user:" + password))
	cases := []struct {
		name        string
		credentials gitea.Credentials
		options     []gitea.Option
		want        map[string]string
	}{
		{"a token", gitea.Token(token), nil, map[string]string{"Authorization": "token " + token}},
		{"Basic", gitea.Basic("synthetic-user", password), nil, map[string]string{"Authorization": "Basic " + encoded}},
		{"Basic with a one-time password", gitea.BasicWithOTP("synthetic-user", password, otp), nil,
			map[string]string{"Authorization": "Basic " + encoded, "X-Gitea-Otp": otp}},
		{"a token and sudo", gitea.Token(token), []gitea.Option{gitea.WithSudo("synthetic-other")},
			map[string]string{"Authorization": "token " + token, "Sudo": "synthetic-other"}},
		{"Basic and sudo", gitea.BasicWithOTP("synthetic-user", password, otp), []gitea.Option{gitea.WithSudo("synthetic-other")},
			map[string]string{"Authorization": "Basic " + encoded, "X-Gitea-Otp": otp, "Sudo": "synthetic-other"}},
	}
	for index, item := range cases {
		t.Run(item.name, func(t *testing.T) {
			client := newClient(t, server.URL, item.credentials, append(item.options, gitea.WithUserAgent("example-app/1.0"))...)
			user, err := client.CurrentUser.Get(context.Background())
			if err != nil || *user.Login != "synthetic-user" {
				t.Fatalf("user is %v, %v", user, err)
			}
			got := record.all()[index]
			if got.uri != "/api/v1/user" || got.header.Get("User-Agent") != "example-app/1.0" || got.header.Get("Accept") != "application/json" {
				t.Fatalf("request is %s %v", got.uri, got.header)
			}
			for _, name := range []string{"Authorization", "X-Gitea-Otp", "Sudo"} {
				if got.header.Get(name) != item.want[name] {
					t.Fatalf("%s is %q, not %q", name, got.header.Get(name), item.want[name])
				}
			}
		})
	}
}

func TestAPathParameterHoldingASlashIsOneSegment(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{"type":"file","path":"docs/guide/intro.md"}`)
	})
	client := newClient(t, server.URL, gitea.Token(token))
	content, err := client.Contents.Get(context.Background(), "synthetic-owner", "synthetic-repo", "docs/guide/intro.md",
		&gitea.ContentsGetParams{Ref: gitea.Ptr("main")})
	if err != nil || *content.Path != "docs/guide/intro.md" {
		t.Fatalf("content is %v, %v", content, err)
	}
	if uri := record.all()[0].uri; uri != "/api/v1/repos/synthetic-owner/synthetic-repo/contents/docs%2Fguide%2Fintro.md?ref=main" {
		t.Fatalf("request is %s", uri)
	}
}

func TestAFailedCallIsTypedAndHoldsNoCredential(t *testing.T) {
	server, _ := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 404, fmt.Sprintf(`{"message":"no repository for %s","url":"https://gitea.example.com/api/swagger"}`, password))
	})
	var logs bytes.Buffer
	logger := slog.New(slog.NewTextHandler(&logs, &slog.HandlerOptions{Level: slog.LevelDebug}))
	client := newClient(t, server.URL, gitea.BasicWithOTP("synthetic-user", password, otp), gitea.WithLogger(logger))
	_, err := client.Repos.Get(context.Background(), "synthetic-owner", "missing")
	var failure *gitea.APIError
	if !errors.Is(err, gitea.ErrNotFound) || !errors.As(err, &failure) {
		t.Fatalf("error is %v", err)
	}
	if failure.Status != 404 || failure.Detail != "no repository for ***" || strings.Contains(failure.RawBody, password) {
		t.Fatalf("error is %+v", failure)
	}
	if failure.Error() != "HTTP 404 (not_found): no repository for ***" {
		t.Fatalf("message is %q", failure.Error())
	}
	encoded := base64.StdEncoding.EncodeToString([]byte("synthetic-user:" + password))
	for _, secret := range []string{password, otp, encoded} {
		if strings.Contains(logs.String(), secret) {
			t.Fatalf("logs hold a secret: %s", logs.String())
		}
	}
	if logs.Len() == 0 {
		t.Fatal("nothing was logged")
	}
}

func TestEachStatusHasItsKind(t *testing.T) {
	statuses := map[int]error{
		400: gitea.ErrBadRequest, 401: gitea.ErrAuthentication, 403: gitea.ErrPermission, 404: gitea.ErrNotFound,
		409: gitea.ErrConflict, 422: gitea.ErrValidation, 429: gitea.ErrRateLimited, 500: gitea.ErrServer, 418: gitea.ErrAPI,
	}
	for status, sentinel := range statuses {
		t.Run(fmt.Sprint(status), func(t *testing.T) {
			server, _ := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
				w.Header().Set("Retry-After", "0")
				replyJSON(w, status, `{"message":"synthetic failure"}`)
			})
			_, err := newClient(t, server.URL, gitea.Token(token), gitea.WithMaxRetries(0)).Misc.GetVersion(context.Background())
			if !errors.Is(err, sentinel) {
				t.Fatalf("error is %v", err)
			}
		})
	}
}

func TestIteratorsFollowTheLinkHeaderWithoutFetchingIt(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		switch r.URL.Query().Get("page") {
		case "":
			w.Header().Add("Link", `<https://elsewhere.example.com/api/v1/repos/o/r/issues?page=2&limit=2&state=open>; rel="next", <https://elsewhere.example.com/api/v1/repos/o/r/issues?page=3&limit=2>; rel="last"`)
			replyJSON(w, 200, `[{"number":1},{"number":2}]`)
		case "2":
			w.Header().Add("Link", `<https://elsewhere.example.com/api/v1/repos/o/r/issues?page=3&limit=2>; rel="next last"`)
			replyJSON(w, 200, `[{"number":3},{"number":4}]`)
		default:
			w.Header().Add("Link", `<https://elsewhere.example.com/api/v1/repos/o/r/issues?page=1&limit=2>; rel="first"`)
			replyJSON(w, 200, `[{"number":5}]`)
		}
	})
	client := newClient(t, server.URL, gitea.Token(token))
	numbers := []int64{}
	for issue, err := range client.Issues.Iter(context.Background(), "o", "r", &gitea.IssuesListParams{State: gitea.Ptr("open"), Limit: gitea.Ptr[int64](2)}) {
		if err != nil {
			t.Fatal(err)
		}
		numbers = append(numbers, *issue.Number)
	}
	if fmt.Sprint(numbers) != "[1 2 3 4 5]" {
		t.Fatalf("numbers are %v", numbers)
	}
	uris := []string{}
	for _, request := range record.all() {
		uris = append(uris, request.uri)
	}
	want := []string{
		"/api/v1/repos/o/r/issues?limit=2&state=open",
		"/api/v1/repos/o/r/issues?limit=2&page=2&state=open",
		"/api/v1/repos/o/r/issues?limit=2&page=3&state=open",
	}
	if strings.Join(uris, " ") != strings.Join(want, " ") {
		t.Fatalf("requests are %v", uris)
	}
}

func TestAPageOfStringsIterates(t *testing.T) {
	server, _ := mock(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		if r.URL.Query().Get("page") == "" {
			w.Header().Set("Link", `<https://gitea.example.com/api/v1/repos/o/r/topics?page=2>; rel="next"`)
			replyJSON(w, 200, `{"topics":["go","sdk"]}`)
			return
		}
		replyJSON(w, 200, `{"topics":["gitea"]}`)
	})
	topics := []string{}
	for topic, err := range newClient(t, server.URL, gitea.Token(token)).Repos.IterTopics(context.Background(), "o", "r", nil) {
		if err != nil {
			t.Fatal(err)
		}
		topics = append(topics, topic)
	}
	if strings.Join(topics, " ") != "go sdk gitea" {
		t.Fatalf("topics are %v", topics)
	}
}

func TestARepeatedNextPageFails(t *testing.T) {
	server, _ := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		w.Header().Set("Link", `<https://gitea.example.com/api/v1/repos/o/r/issues?page=2>; rel="next"`)
		replyJSON(w, 200, `[{"number":1}]`)
	})
	var last error
	for _, err := range newClient(t, server.URL, gitea.Token(token)).Issues.Iter(context.Background(), "o", "r", nil) {
		last = err
	}
	if !errors.Is(last, gitea.ErrDecode) {
		t.Fatalf("error is %v", last)
	}
}

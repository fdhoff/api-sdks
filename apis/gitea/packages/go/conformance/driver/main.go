// Command driver is the conformance driver: it reads cases as JSON lines and calls the public client.
// See the runner's README.
//
// The client adds /api/v1 to the instance URL, while the cases name each path as the spec declares
// it, because the mock serves them without the prefix. The driver's transport removes the prefix on
// the way out. A request without it goes out unchanged, so its path fails the case's wire check.
package main

import (
	"bufio"
	"context"
	"encoding/base64"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log"
	"log/slog"
	"net/http"
	"os"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/fdhoff/api-sdks/apis/gitea/packages/go/gitearest"
	"github.com/fdhoff/api-sdks/apis/gitea/packages/go/internal/runtime"
)

type settings struct {
	BaseURL          string  `json:"base_url"`
	Token            string  `json:"token"`
	Username         *string `json:"username"`
	Password         string  `json:"password"`
	OTP              *string `json:"otp"`
	Sudo             *string `json:"sudo"`
	UserAgent        string  `json:"user_agent"`
	TimeoutMS        *int64  `json:"timeout_ms"`
	MaxRetries       *int    `json:"max_retries"`
	RetryBaseDelayMS *int64  `json:"retry_base_delay_ms"`
	RateLimitWaitMS  *int64  `json:"rate_limit_wait_ms"`
	MaxRetryWaitMS   *int64  `json:"max_retry_wait_ms"`
}

type request struct {
	Operation string          `json:"operation"`
	Params    map[string]any  `json:"params"`
	Body      json.RawMessage `json:"body"`
	Fields    map[string]any  `json:"-"`
	Multipart map[string]any  `json:"multipart"`
	Paginate  bool            `json:"paginate"`
}

type message struct {
	Client  settings `json:"client"`
	Request request  `json:"request"`
}

type capture struct {
	mutex sync.Mutex
	lines []string
}

func (c *capture) Enabled(context.Context, slog.Level) bool { return true }
func (c *capture) WithAttrs([]slog.Attr) slog.Handler       { return c }
func (c *capture) WithGroup(string) slog.Handler            { return c }

func (c *capture) Handle(_ context.Context, record slog.Record) error {
	line := []string{record.Message}
	record.Attrs(func(attr slog.Attr) bool {
		line = append(line, attr.String())
		return true
	})
	c.mutex.Lock()
	defer c.mutex.Unlock()
	c.lines = append(c.lines, strings.Join(line, " "))
	return nil
}

// unprefixed removes the client's /api/v1 from each request on its way to the mock.
type unprefixed struct{}

func (unprefixed) RoundTrip(request *http.Request) (*http.Response, error) {
	if strings.HasPrefix(request.URL.Path, gitearest.APIPath+"/") {
		address := *request.URL
		address.Path = strings.TrimPrefix(address.Path, gitearest.APIPath)
		address.RawPath = strings.TrimPrefix(address.RawPath, gitearest.APIPath)
		request = request.Clone(request.Context())
		request.URL = &address
	}
	return http.DefaultTransport.RoundTrip(request)
}

func milliseconds(value *int64, option func(time.Duration) gitearest.Option) []gitearest.Option {
	if value == nil {
		return nil
	}
	return []gitearest.Option{option(time.Duration(*value) * time.Millisecond)}
}

// credentials uses Basic when the case sets a username, with the one-time password unless it is
// null, and the token otherwise.
func credentials(config settings) gitearest.Credentials {
	switch {
	case config.Username == nil:
		return gitearest.Token(config.Token)
	case config.OTP == nil:
		return gitearest.Basic(*config.Username, config.Password)
	default:
		return gitearest.BasicWithOTP(*config.Username, config.Password, *config.OTP)
	}
}

func newClient(config settings, logs *capture) (*gitearest.Client, error) {
	options := []gitearest.Option{gitearest.WithLogger(slog.New(logs)), gitearest.WithHTTPTransport(unprefixed{})}
	if config.Sudo != nil {
		options = append(options, gitearest.WithSudo(*config.Sudo))
	}
	if config.UserAgent != "" {
		options = append(options, gitearest.WithUserAgent(config.UserAgent))
	}
	options = append(options, milliseconds(config.TimeoutMS, gitearest.WithTimeout)...)
	options = append(options, milliseconds(config.RetryBaseDelayMS, gitearest.WithRetryBaseDelay)...)
	options = append(options, milliseconds(config.RateLimitWaitMS, gitearest.WithRateLimitWait)...)
	options = append(options, milliseconds(config.MaxRetryWaitMS, gitearest.WithMaxRetryWait)...)
	if config.MaxRetries != nil {
		options = append(options, gitearest.WithMaxRetries(*config.MaxRetries))
	}
	return gitearest.NewClient(config.BaseURL, credentials(config), options...)
}

// assign puts a JSON value into a typed target. Cases give numbers and strings by wire form, so
// when the type disagrees with the case, the value is retried as the other of the two. A string
// given for a model, such as a multipart JSON part, is decoded as the JSON it holds.
func assign(target reflect.Value, value any) error {
	encoded, err := json.Marshal(value)
	if err != nil {
		return err
	}
	if json.Unmarshal(encoded, target.Addr().Interface()) == nil {
		return nil
	}
	retry := strconv.Quote(strings.Trim(string(encoded), `"`))
	if text, isText := value.(string); isText {
		retry = text
	}
	return json.Unmarshal([]byte(retry), target.Addr().Interface())
}

var (
	fileType  = reflect.TypeFor[gitearest.File]()
	filesType = reflect.TypeFor[[]gitearest.File]()
)

// files reads file fields, which arrive as strings and are sent as their content.
func files(value any) ([]gitearest.File, error) {
	items, isList := value.([]any)
	if !isList {
		items = []any{value}
	}
	result := make([]gitearest.File, 0, len(items))
	for _, item := range items {
		text, isText := item.(string)
		if !isText {
			encoded, err := json.Marshal(item)
			if err != nil {
				return nil, err
			}
			text = string(encoded)
		}
		result = append(result, gitearest.File{Content: []byte(text)})
	}
	return result, nil
}

// isParams reports whether a method argument is a params struct: one with a field of any params tag.
func isParams(shape reflect.Type) bool {
	if shape.Kind() != reflect.Pointer || shape.Elem().Kind() != reflect.Struct {
		return false
	}
	for index := range shape.Elem().NumField() {
		tag := shape.Elem().Field(index).Tag
		if tag.Get("query") != "" || tag.Get("header") != "" || tag.Get("form") != "" || tag.Get("urlencoded") != "" {
			return true
		}
	}
	return false
}

// isForm reports whether a params struct carries a form body, whose fields a case gives as its body.
func isForm(shape reflect.Type) bool {
	for index := range shape.Elem().NumField() {
		tag := shape.Elem().Field(index).Tag
		if tag.Get("form") != "" || tag.Get("urlencoded") != "" {
			return true
		}
	}
	return false
}

func paramsArgument(shape reflect.Type, req request) (reflect.Value, error) {
	params := reflect.New(shape.Elem())
	for index := range shape.Elem().NumField() {
		field := shape.Elem().Field(index)
		wire, values := field.Tag.Get("query"), req.Params
		switch {
		case field.Tag.Get("header") != "":
			wire = field.Tag.Get("header")
		case field.Tag.Get("form") != "":
			wire, values = field.Tag.Get("form"), req.Multipart
		case field.Tag.Get("urlencoded") != "":
			wire, values = field.Tag.Get("urlencoded"), req.Fields
		}
		value, found := values[wire]
		if !found {
			continue
		}
		if field.Type == filesType || field.Type == fileType {
			content, err := files(value)
			if err != nil {
				return params, fmt.Errorf("%s: %w", wire, err)
			}
			if field.Type == fileType {
				if len(content) != 1 {
					return params, fmt.Errorf("%s: expected one file", wire)
				}
				params.Elem().Field(index).Set(reflect.ValueOf(content[0]))
				continue
			}
			params.Elem().Field(index).Set(reflect.ValueOf(content))
			continue
		}
		if err := assign(params.Elem().Field(index), value); err != nil {
			return params, fmt.Errorf("%s: %w", wire, err)
		}
	}
	return params, nil
}

func arguments(method reflect.Type, operation *runtime.Operation, req request) ([]reflect.Value, error) {
	args := []reflect.Value{reflect.ValueOf(context.Background())}
	for _, name := range operation.PathParams {
		value := reflect.New(method.In(len(args))).Elem()
		if err := assign(value, req.Params[name]); err != nil {
			return nil, fmt.Errorf("%s: %w", name, err)
		}
		args = append(args, value)
	}
	for len(args) < method.NumIn() {
		shape := method.In(len(args))
		if isParams(shape) {
			if isForm(shape) && req.Body != nil {
				if err := json.Unmarshal(req.Body, &req.Fields); err != nil {
					return nil, err
				}
				if req.Multipart == nil {
					req.Multipart = req.Fields
				}
			}
			params, err := paramsArgument(shape, req)
			if err != nil {
				return nil, err
			}
			args = append(args, params)
			continue
		}
		body := reflect.Zero(shape)
		if req.Body != nil {
			body = reflect.New(shape.Elem())
			if err := json.Unmarshal(req.Body, body.Interface()); err != nil {
				return nil, err
			}
		}
		args = append(args, body)
	}
	return args, nil
}

func call(client *gitearest.Client, req request) (any, error) {
	operation, found := runtime.Lookup(req.Operation)
	if !found {
		log.Fatalf("unknown operation %s", req.Operation)
	}
	name := operation.Name
	if req.Paginate {
		name = operation.Iterator
	}
	resource := reflect.ValueOf(client).Elem().FieldByName(operation.Resource)
	method := resource.MethodByName(name)
	args, err := arguments(method.Type(), operation, req)
	if err != nil {
		log.Fatalf("%s: %v", req.Operation, err)
	}
	results := method.Call(args)
	if req.Paginate {
		items := []any{}
		for item, failure := range results[0].Seq2() {
			if !failure.IsNil() {
				return nil, failure.Interface().(error)
			}
			items = append(items, item.Interface())
		}
		return items, nil
	}
	if failure := results[len(results)-1]; !failure.IsNil() {
		return nil, failure.Interface().(error)
	}
	if len(results) == 1 {
		return nil, nil
	}
	if download, isDownload := results[0].Interface().(*gitearest.Download); isDownload {
		return downloadOutput(download)
	}
	return results[0].Interface(), nil
}

func downloadOutput(download *gitearest.Download) (any, error) {
	defer download.Body.Close()
	body, err := io.ReadAll(download.Body)
	if err != nil {
		return nil, err
	}
	return map[string]string{"content_type": download.ContentType, "base64": base64.StdEncoding.EncodeToString(body)}, nil
}

func errorOutput(failure *gitearest.APIError) map[string]any {
	output := map[string]any{"kind": failure.Kind}
	if failure.Status != 0 {
		output["status"] = failure.Status
		output["raw_body"] = failure.RawBody
	}
	if failure.Detail != "" {
		output["message"] = failure.Detail
	}
	return output
}

func run(line []byte) map[string]any {
	var input message
	if err := json.Unmarshal(line, &input); err != nil {
		log.Fatal(err)
	}
	logs := &capture{lines: []string{}}
	client, err := newClient(input.Client, logs)
	if err != nil {
		log.Fatal(err)
	}
	result, err := call(client, input.Request)
	if err == nil {
		return map[string]any{"result": result, "logs": logs.lines}
	}
	var failure *gitearest.APIError
	if !errors.As(err, &failure) {
		log.Fatal(err)
	}
	return map[string]any{"error": errorOutput(failure), "logs": logs.lines}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1024*1024), 64*1024*1024)
	output := json.NewEncoder(os.Stdout)
	for scanner.Scan() {
		if err := output.Encode(run(scanner.Bytes())); err != nil {
			log.Fatal(err)
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

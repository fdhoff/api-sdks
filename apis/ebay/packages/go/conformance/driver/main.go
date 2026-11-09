// Command driver is the conformance driver: it reads cases as JSON lines and calls the public client.
// See the runner's README.
package main

import (
	"bufio"
	"context"
	"crypto/ed25519"
	"crypto/rand"
	"crypto/x509"
	"encoding/json"
	"encoding/pem"
	"errors"
	"fmt"
	"log"
	"log/slog"
	"net/url"
	"os"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/internal/runtime"
)

type settings struct {
	BaseURL          string            `json:"base_url"`
	AppToken         string            `json:"app_token"`
	UserToken        string            `json:"user_token"`
	Environment      string            `json:"environment"`
	HeaderDefaults   map[string]string `json:"header_defaults"`
	SignatureKey     string            `json:"signature_key"`
	UserAgent        string            `json:"user_agent"`
	TimeoutMS        *int64            `json:"timeout_ms"`
	MaxRetries       *int              `json:"max_retries"`
	RetryBaseDelayMS *int64            `json:"retry_base_delay_ms"`
	RateLimitWaitMS  *int64            `json:"rate_limit_wait_ms"`
	MaxRetryWaitMS   *int64            `json:"max_retry_wait_ms"`
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

func milliseconds(value *int64, option func(time.Duration) ebaysell.Option) []ebaysell.Option {
	if value == nil {
		return nil
	}
	return []ebaysell.Option{option(time.Duration(*value) * time.Millisecond)}
}

// Each contract's name in the cases, and the client field that holds it.
var contracts = map[string]string{
	"sell_account_v1":          "Account",
	"sell_account_v2":          "AccountV2",
	"sell_analytics":           "Analytics",
	"sell_feed":                "Feed",
	"sell_finances":            "Finances",
	"sell_fulfillment":         "Fulfillment",
	"sell_inventory":           "Inventory",
	"sell_marketing":           "Marketing",
	"sell_metadata":            "Metadata",
	"sell_negotiation":         "Negotiation",
	"sell_recommendation":      "Recommendation",
	"sell_stores":              "Stores",
	"sell_post_order":          "PostOrder",
	"commerce_feedback":        "Feedback",
	"commerce_identity":        "Identity",
	"commerce_media":           "Media",
	"commerce_message":         "Message",
	"commerce_notification":    "Notification",
	"commerce_taxonomy":        "Taxonomy",
	"developer_analytics":      "DeveloperAnalytics",
	"developer_key_management": "KeyManagement",
}

// privateKey is generated per run, never stored: the cases check the signature's shape and digest,
// not the key.
var privateKey = func() string {
	_, key, err := ed25519.GenerateKey(rand.Reader)
	if err != nil {
		log.Fatal(err)
	}
	encoded, err := x509.MarshalPKCS8PrivateKey(key)
	if err != nil {
		log.Fatal(err)
	}
	return string(pem.EncodeToMemory(&pem.Block{Type: "PRIVATE KEY", Bytes: encoded}))
}()

// hosts maps each host key to its harness prefix: the key itself, or with an environment the
// hostname that environment gives the key.
func hosts(config settings) map[string]string {
	environment := config.Environment
	if environment == "" {
		environment = ebaysell.Production
	}
	mapped := map[string]string{}
	for key, base := range ebaysell.Environments()[environment] {
		name := key
		if config.Environment != "" {
			parsed, err := url.Parse(base)
			if err != nil {
				log.Fatal(err)
			}
			name = parsed.Hostname()
		}
		mapped[key] = config.BaseURL + "/_host/" + name
	}
	return mapped
}

func newClient(config settings, logs *capture) (*ebaysell.Client, error) {
	options := []ebaysell.Option{
		ebaysell.WithHosts(hosts(config)),
		ebaysell.WithLogger(slog.New(logs)),
		ebaysell.WithAppToken(config.AppToken),
		ebaysell.WithUserToken(config.UserToken),
		ebaysell.WithMarketplaceID(config.HeaderDefaults["X-EBAY-C-MARKETPLACE-ID"]),
		ebaysell.WithContentLanguage(config.HeaderDefaults["Content-Language"]),
	}
	if config.Environment != "" {
		options = append(options, ebaysell.WithEnvironment(config.Environment))
	}
	if config.SignatureKey != "" {
		options = append(options, ebaysell.WithSigningKey(ebaysell.SigningKey{PrivateKey: privateKey, JWE: config.SignatureKey}))
	}
	if config.UserAgent != "" {
		options = append(options, ebaysell.WithUserAgent(config.UserAgent))
	}
	options = append(options, milliseconds(config.TimeoutMS, ebaysell.WithTimeout)...)
	options = append(options, milliseconds(config.RetryBaseDelayMS, ebaysell.WithRetryBaseDelay)...)
	options = append(options, milliseconds(config.RateLimitWaitMS, ebaysell.WithRateLimitWait)...)
	options = append(options, milliseconds(config.MaxRetryWaitMS, ebaysell.WithMaxRetryWait)...)
	if config.MaxRetries != nil {
		options = append(options, ebaysell.WithMaxRetries(*config.MaxRetries))
	}
	return ebaysell.NewClient(options...)
}

// assign puts a JSON value into a typed target. Cases give numbers and strings by wire form, so
// when the type disagrees with the case, the value is retried as the other of the two.
func assign(target reflect.Value, value any) error {
	encoded, err := json.Marshal(value)
	if err != nil {
		return err
	}
	if json.Unmarshal(encoded, target.Addr().Interface()) == nil {
		return nil
	}
	retry := strconv.Quote(strings.Trim(string(encoded), `"`))
	if _, isText := value.(string); isText {
		retry = strings.Trim(string(encoded), `"`)
	}
	return json.Unmarshal([]byte(retry), target.Addr().Interface())
}

var (
	fileType  = reflect.TypeFor[ebaysell.File]()
	filesType = reflect.TypeFor[[]ebaysell.File]()
)

// files reads file fields, which arrive as strings and are sent as their content.
func files(value any) ([]ebaysell.File, error) {
	items, isList := value.([]any)
	if !isList {
		items = []any{value}
	}
	result := make([]ebaysell.File, 0, len(items))
	for _, item := range items {
		text, isText := item.(string)
		if !isText {
			encoded, err := json.Marshal(item)
			if err != nil {
				return nil, err
			}
			text = string(encoded)
		}
		result = append(result, ebaysell.File{Content: []byte(text)})
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

func call(client *ebaysell.Client, req request) (any, error) {
	operation, found := runtime.Lookup(req.Operation)
	if !found {
		log.Fatalf("unknown operation %s", req.Operation)
	}
	name := operation.Name
	if req.Paginate {
		name = operation.Iterator
	}
	api := reflect.ValueOf(client).Elem().FieldByName(contracts[operation.Contract])
	method := api.FieldByName(operation.Resource).MethodByName(name)
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
	return results[0].Interface(), nil
}

func errorOutput(failure *ebaysell.APIError) map[string]any {
	output := map[string]any{"kind": failure.Kind}
	if failure.Status != 0 {
		output["status"] = failure.Status
	}
	for name, value := range map[string]string{
		"raw_body": failure.RawBody,
		"message":  failure.Detail,
	} {
		if value != "" {
			output[name] = value
		}
	}
	if code, err := strconv.ParseInt(failure.Code, 10, 64); err == nil {
		output["code"] = code
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
	var failure *ebaysell.APIError
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

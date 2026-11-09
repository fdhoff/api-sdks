// Command driver is the conformance driver: it reads cases as JSON lines and calls the public client.
// See the runner's README.
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
	"net/url"
	"os"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/fdhoff/api-sdks/apis/mercury/packages/go/internal/runtime"
	"github.com/fdhoff/api-sdks/apis/mercury/packages/go/mercurybanking"
)

type settings struct {
	BaseURL          string `json:"base_url"`
	Token            string `json:"token"`
	Environment      string `json:"environment"`
	UserAgent        string `json:"user_agent"`
	TimeoutMS        *int64 `json:"timeout_ms"`
	MaxRetries       *int   `json:"max_retries"`
	RetryBaseDelayMS *int64 `json:"retry_base_delay_ms"`
	RateLimitWaitMS  *int64 `json:"rate_limit_wait_ms"`
	MaxRetryWaitMS   *int64 `json:"max_retry_wait_ms"`
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

func milliseconds(value *int64, option func(time.Duration) mercurybanking.Option) []mercurybanking.Option {
	if value == nil {
		return nil
	}
	return []mercurybanking.Option{option(time.Duration(*value) * time.Millisecond)}
}

// hosts maps each host key to its harness prefix: the key itself, or with an environment the
// hostname that environment gives the key.
func hosts(config settings) map[string]string {
	environment := config.Environment
	if environment == "" {
		environment = mercurybanking.Production
	}
	mapped := map[string]string{}
	for key, base := range mercurybanking.Environments()[environment] {
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

func newClient(config settings, logs *capture) (*mercurybanking.Client, error) {
	options := []mercurybanking.Option{
		mercurybanking.WithHosts(hosts(config)),
		mercurybanking.WithLogger(slog.New(logs)),
	}
	if config.Environment != "" {
		options = append(options, mercurybanking.WithEnvironment(config.Environment))
	}
	if config.UserAgent != "" {
		options = append(options, mercurybanking.WithUserAgent(config.UserAgent))
	}
	options = append(options, milliseconds(config.TimeoutMS, mercurybanking.WithTimeout)...)
	options = append(options, milliseconds(config.RetryBaseDelayMS, mercurybanking.WithRetryBaseDelay)...)
	options = append(options, milliseconds(config.RateLimitWaitMS, mercurybanking.WithRateLimitWait)...)
	options = append(options, milliseconds(config.MaxRetryWaitMS, mercurybanking.WithMaxRetryWait)...)
	if config.MaxRetries != nil {
		options = append(options, mercurybanking.WithMaxRetries(*config.MaxRetries))
	}
	return mercurybanking.NewClient(config.Token, options...)
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
	fileType  = reflect.TypeFor[mercurybanking.File]()
	filesType = reflect.TypeFor[[]mercurybanking.File]()
)

// files reads file fields, which arrive as strings and are sent as their content.
func files(value any) ([]mercurybanking.File, error) {
	items, isList := value.([]any)
	if !isList {
		items = []any{value}
	}
	result := make([]mercurybanking.File, 0, len(items))
	for _, item := range items {
		text, isText := item.(string)
		if !isText {
			encoded, err := json.Marshal(item)
			if err != nil {
				return nil, err
			}
			text = string(encoded)
		}
		result = append(result, mercurybanking.File{Content: []byte(text)})
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

func call(client *mercurybanking.Client, req request) (any, error) {
	operation, found := runtime.Lookup(req.Operation)
	if !found {
		log.Fatalf("unknown operation %s", req.Operation)
	}
	name := operation.Name
	if req.Paginate {
		name = operation.Iterator
	}
	method := reflect.ValueOf(client).Elem().FieldByName(operation.Resource).MethodByName(name)
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
	if download, isDownload := results[0].Interface().(*mercurybanking.Download); isDownload {
		return downloadOutput(download)
	}
	return results[0].Interface(), nil
}

func downloadOutput(download *mercurybanking.Download) (any, error) {
	defer download.Body.Close()
	body, err := io.ReadAll(download.Body)
	if err != nil {
		return nil, err
	}
	return map[string]string{"content_type": download.ContentType, "base64": base64.StdEncoding.EncodeToString(body)}, nil
}

func errorOutput(failure *mercurybanking.APIError) map[string]any {
	output := map[string]any{"kind": failure.Kind}
	if failure.Status != 0 {
		output["status"] = failure.Status
		output["raw_body"] = failure.RawBody
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
	var failure *mercurybanking.APIError
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

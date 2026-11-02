// Command driver is the conformance driver: it reads cases as JSON lines and calls the public client.
// See the runner's README.
package main

import (
	"bufio"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"log/slog"
	"os"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/fdhoff/backmarket-seller-sdk/apis/backmarket/packages/go/backmarketseller"
	"github.com/fdhoff/backmarket-seller-sdk/apis/backmarket/packages/go/internal/runtime"
)

type settings struct {
	BaseURL          string `json:"base_url"`
	Token            string `json:"token"`
	UserAgent        string `json:"user_agent"`
	Locale           string `json:"locale"`
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

func milliseconds(value *int64, option func(time.Duration) backmarketseller.Option) []backmarketseller.Option {
	if value == nil {
		return nil
	}
	return []backmarketseller.Option{option(time.Duration(*value) * time.Millisecond)}
}

func newClient(config settings, logs *capture) (*backmarketseller.Client, error) {
	options := []backmarketseller.Option{
		backmarketseller.WithBaseURL(config.BaseURL),
		backmarketseller.WithLogger(slog.New(logs)),
	}
	options = append(options, milliseconds(config.TimeoutMS, backmarketseller.WithTimeout)...)
	options = append(options, milliseconds(config.RetryBaseDelayMS, backmarketseller.WithRetryBaseDelay)...)
	options = append(options, milliseconds(config.RateLimitWaitMS, backmarketseller.WithRateLimitWait)...)
	options = append(options, milliseconds(config.MaxRetryWaitMS, backmarketseller.WithMaxRetryWait)...)
	if config.MaxRetries != nil {
		options = append(options, backmarketseller.WithMaxRetries(*config.MaxRetries))
	}
	return backmarketseller.NewClient(config.Token, config.UserAgent, config.Locale, options...)
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

func isParams(shape reflect.Type) bool {
	if shape.Kind() != reflect.Pointer || shape.Elem().Kind() != reflect.Struct || shape.Elem().NumField() == 0 {
		return false
	}
	tag := shape.Elem().Field(0).Tag
	return tag.Get("query") != "" || tag.Get("form") != ""
}

func paramsArgument(shape reflect.Type, req request) (reflect.Value, error) {
	params := reflect.New(shape.Elem())
	for index := range shape.Elem().NumField() {
		field := shape.Elem().Field(index)
		wire, values := field.Tag.Get("query"), req.Params
		if wire == "" {
			wire, values = field.Tag.Get("form"), req.Multipart
		}
		value, found := values[wire]
		if !found {
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

func call(client *backmarketseller.Client, req request) (any, error) {
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
	return results[0].Interface(), nil
}

func errorOutput(failure *backmarketseller.APIError) map[string]any {
	output := map[string]any{"kind": failure.Kind}
	if failure.Status != 0 {
		output["status"] = failure.Status
	}
	for name, value := range map[string]string{
		"raw_body":   failure.RawBody,
		"code":       failure.Code,
		"request_id": failure.RequestID,
		"cf_ray":     failure.CFRay,
	} {
		if value != "" {
			output[name] = value
		}
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
	var failure *backmarketseller.APIError
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

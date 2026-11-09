package runtime

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"mime/multipart"
	"net/url"
	"reflect"
	"strconv"
	"strings"
	"time"
)

// File is a file to upload. Name defaults to the form field's name.
type File struct {
	Name    string
	Content []byte
}

// Input is one call's arguments: path values in order, a pointer to a struct of fields tagged
// `query`, `header`, `form` for a multipart part or `urlencoded` for a form-encoded field, and a JSON body.
// Raw is a raw body for an operation with [Operation.RawBody], sent unchanged and never closed.
type Input struct {
	Path   []any
	Params any
	Body   any
	Raw    io.Reader
}

type request struct {
	operation *Operation
	method    string
	path      string
	query     url.Values
	// headers holds the header arguments passed to the call, by wire name.
	headers     url.Values
	body        []byte
	contentType string
	// stream is a raw body that can be read only once, so it is never resent.
	stream io.Reader
}

func (r *request) url(base string) string {
	if len(r.query) == 0 {
		return base + r.path
	}
	return base + r.path + "?" + r.query.Encode()
}

func text(value reflect.Value) string {
	if moment, ok := value.Interface().(time.Time); ok {
		return moment.Format(time.RFC3339)
	}
	switch value.Kind() {
	case reflect.String:
		return value.String()
	case reflect.Bool:
		return strconv.FormatBool(value.Bool())
	case reflect.Float32, reflect.Float64:
		return strconv.FormatFloat(value.Float(), 'f', -1, value.Type().Bits())
	default:
		return fmt.Sprint(value.Interface())
	}
}

func isNil(value reflect.Value) bool {
	switch value.Kind() {
	case reflect.Invalid:
		return true
	case reflect.Pointer, reflect.Slice, reflect.Map, reflect.Interface:
		return value.IsNil()
	default:
		return false
	}
}

func indirect(value reflect.Value) reflect.Value {
	for value.Kind() == reflect.Pointer || value.Kind() == reflect.Interface {
		value = value.Elem()
	}
	return value
}

func addPart(form *multipart.Writer, wire string, value reflect.Value) error {
	value = indirect(value)
	if value.Kind() == reflect.Slice && value.Type().Elem().Kind() != reflect.Uint8 {
		for index := range value.Len() {
			if err := addPart(form, wire, value.Index(index)); err != nil {
				return err
			}
		}
		return nil
	}
	switch item := value.Interface().(type) {
	case File:
		name := item.Name
		if name == "" {
			name = wire
		}
		part, err := form.CreateFormFile(wire, name)
		if err != nil {
			return err
		}
		_, err = part.Write(item.Content)
		return err
	case []byte:
		return addPart(form, wire, reflect.ValueOf(File{Content: item}))
	case time.Time:
		return form.WriteField(wire, text(value))
	}
	if kind := value.Kind(); kind == reflect.Struct || kind == reflect.Map {
		encoded, err := json.Marshal(value.Interface())
		if err != nil {
			return err
		}
		return form.WriteField(wire, string(encoded))
	}
	return form.WriteField(wire, text(value))
}

// addValues adds a field once per item when it is a list. A struct or map is sent as JSON.
func addValues(values url.Values, wire string, field reflect.Value) error {
	item := indirect(field)
	if item.Kind() == reflect.Slice {
		for position := range item.Len() {
			if err := addValues(values, wire, item.Index(position)); err != nil {
				return err
			}
		}
		return nil
	}
	if _, isTime := item.Interface().(time.Time); !isTime && (item.Kind() == reflect.Struct || item.Kind() == reflect.Map) {
		encoded, err := json.Marshal(item.Interface())
		if err != nil {
			return err
		}
		values.Add(wire, string(encoded))
		return nil
	}
	values.Add(wire, text(item))
	return nil
}

func (r *request) addParams(params any) error {
	source := indirect(reflect.ValueOf(params))
	if !source.IsValid() {
		return nil
	}
	var buffer bytes.Buffer
	form := multipart.NewWriter(&buffer)
	hasParts := false
	fields := url.Values{}
	shape := source.Type()
	for index := range shape.NumField() {
		field := source.Field(index)
		if isNil(field) || field.IsZero() {
			continue
		}
		tag := shape.Field(index).Tag
		if wire := tag.Get("query"); wire != "" {
			if err := addValues(r.query, wire, field); err != nil {
				return err
			}
			continue
		}
		if wire := tag.Get("header"); wire != "" {
			if err := addValues(r.headers, wire, field); err != nil {
				return err
			}
			continue
		}
		if wire := tag.Get("urlencoded"); wire != "" {
			if err := addValues(fields, wire, field); err != nil {
				return err
			}
			continue
		}
		hasParts = true
		if err := addPart(form, tag.Get("form"), field); err != nil {
			return err
		}
	}
	if len(fields) > 0 && hasParts {
		return errors.New("form-encoded and multipart fields cannot be sent in one request")
	}
	if len(fields) > 0 {
		r.body = []byte(fields.Encode())
		r.contentType = "application/x-www-form-urlencoded"
		return nil
	}
	if !hasParts {
		return nil
	}
	if err := form.Close(); err != nil {
		return err
	}
	r.body = buffer.Bytes()
	r.contentType = form.FormDataContentType()
	return nil
}

// setRaw keeps a body held in memory as bytes, as net/http does, so it can be resent and signed.
// Any other reader is streamed once and left open: the caller closes it.
func (r *request) setRaw(raw io.Reader) error {
	r.contentType = r.operation.RawBody
	if r.contentType == "" {
		r.contentType = "application/octet-stream"
	}
	switch raw.(type) {
	case *bytes.Reader, *bytes.Buffer, *strings.Reader:
		body, err := io.ReadAll(raw)
		if err != nil {
			return fmt.Errorf("the request body cannot be read: %w", err)
		}
		r.body = body
	default:
		r.stream = io.NopCloser(raw)
	}
	return nil
}

func newRequest(operation *Operation, input Input) (*request, error) {
	path := operation.Path
	for index, name := range operation.PathParams {
		value := url.PathEscape(text(reflect.ValueOf(input.Path[index])))
		path = strings.ReplaceAll(path, "{"+name+"}", value)
	}
	built := &request{operation: operation, method: operation.Method, path: path, query: url.Values{}, headers: url.Values{}}
	if err := built.addParams(input.Params); err != nil {
		return nil, fmt.Errorf("the request cannot be encoded: %w", err)
	}
	if input.Raw != nil && !isNil(reflect.ValueOf(input.Raw)) {
		return built, built.setRaw(input.Raw)
	}
	if input.Body == nil || isNil(reflect.ValueOf(input.Body)) {
		return built, nil
	}
	body, err := json.Marshal(input.Body)
	if err != nil {
		return nil, fmt.Errorf("the request body cannot be encoded: %w", err)
	}
	built.body = body
	built.contentType = "application/json"
	return built, nil
}

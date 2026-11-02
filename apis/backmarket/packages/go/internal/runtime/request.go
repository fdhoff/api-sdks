package runtime

import (
	"bytes"
	"encoding/json"
	"fmt"
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

// Input is one call's arguments: path values in order, a pointer to a struct of tagged query or
// form fields, and a JSON body.
type Input struct {
	Path   []any
	Params any
	Body   any
}

type request struct {
	method      string
	path        string
	query       url.Values
	body        []byte
	contentType string
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

func (r *request) addParams(params any) error {
	source := indirect(reflect.ValueOf(params))
	if !source.IsValid() {
		return nil
	}
	var buffer bytes.Buffer
	form := multipart.NewWriter(&buffer)
	hasParts := false
	shape := source.Type()
	for index := range shape.NumField() {
		field := source.Field(index)
		if isNil(field) || field.IsZero() {
			continue
		}
		if wire := shape.Field(index).Tag.Get("query"); wire != "" {
			item := indirect(field)
			if item.Kind() != reflect.Slice {
				r.query.Add(wire, text(item))
				continue
			}
			for position := range item.Len() {
				r.query.Add(wire, text(indirect(item.Index(position))))
			}
			continue
		}
		hasParts = true
		if err := addPart(form, shape.Field(index).Tag.Get("form"), field); err != nil {
			return err
		}
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

func newRequest(operation *Operation, input Input) (*request, error) {
	path := operation.Path
	for index, name := range operation.PathParams {
		value := url.PathEscape(text(reflect.ValueOf(input.Path[index])))
		path = strings.ReplaceAll(path, "{"+name+"}", value)
	}
	built := &request{method: operation.Method, path: path, query: url.Values{}}
	if err := built.addParams(input.Params); err != nil {
		return nil, fmt.Errorf("the request cannot be encoded: %w", err)
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

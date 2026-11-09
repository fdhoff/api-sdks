package runtime

import (
	"encoding/json"
	"reflect"
	"strings"
)

const extraField = "Extra"

func jsonName(field reflect.StructField) string {
	name, _, _ := strings.Cut(field.Tag.Get("json"), ",")
	if name == "-" {
		return ""
	}
	return name
}

// DecodeObject fills the struct behind model tolerantly, because the spec has not been confirmed
// against the live API. A null, a value that does not fit its field and an unknown field all land
// in Extra, so nothing is lost. Only a value that is not an object at all is an error.
func DecodeObject(data []byte, model any) error {
	var fields map[string]json.RawMessage
	if err := json.Unmarshal(data, &fields); err != nil {
		return err
	}
	if fields == nil {
		return nil
	}
	target := reflect.ValueOf(model).Elem()
	shape := target.Type()
	for index := range shape.NumField() {
		name := jsonName(shape.Field(index))
		raw, found := fields[name]
		if name == "" || !found || string(raw) == "null" {
			continue
		}
		field := target.Field(index)
		if json.Unmarshal(raw, field.Addr().Interface()) == nil {
			delete(fields, name)
		} else {
			field.SetZero()
		}
	}
	if len(fields) > 0 {
		target.FieldByName(extraField).Set(reflect.ValueOf(fields))
	}
	return nil
}

// EncodeObject writes Extra, then every field that is set, so a field set after decoding wins.
func EncodeObject(model any) ([]byte, error) {
	source := reflect.ValueOf(model)
	shape := source.Type()
	fields := map[string]json.RawMessage{}
	for key, value := range source.FieldByName(extraField).Interface().(map[string]json.RawMessage) {
		fields[key] = value
	}
	for index := range shape.NumField() {
		name := jsonName(shape.Field(index))
		field := source.Field(index)
		if name == "" || field.IsZero() {
			continue
		}
		encoded, err := json.Marshal(field.Interface())
		if err != nil {
			return nil, err
		}
		fields[name] = encoded
	}
	return json.Marshal(fields)
}

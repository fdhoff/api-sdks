package runtime

import (
	"net/url"
	"testing"
)

type formParams struct {
	Legacy *bool          `query:"legacy"`
	Title  *string        `urlencoded:"title"`
	Tags   []string       `urlencoded:"tags"`
	Price  *float64       `urlencoded:"price"`
	Meta   map[string]int `urlencoded:"meta"`
	Unset  *string        `urlencoded:"unset"`
}

func TestURLEncodedFieldsAreAFormBody(t *testing.T) {
	title, price, legacy := "a b&c", 1.5, true
	operation := &Operation{ID: "update", Method: "PATCH", Path: "/items"}
	params := &formParams{Legacy: &legacy, Title: &title, Tags: []string{"x", "y"}, Price: &price, Meta: map[string]int{"n": 1}}
	built, err := newRequest(operation, Input{Params: params})
	if err != nil {
		t.Fatal(err)
	}
	if built.contentType != "application/x-www-form-urlencoded" {
		t.Errorf("content type is %q", built.contentType)
	}
	form, err := url.ParseQuery(string(built.body))
	if err != nil {
		t.Fatal(err)
	}
	want := url.Values{"title": {"a b&c"}, "tags": {"x", "y"}, "price": {"1.5"}, "meta": {`{"n":1}`}}
	if form.Encode() != want.Encode() {
		t.Errorf("form is %v", form)
	}
	if built.query.Encode() != "legacy=true" {
		t.Errorf("query is %q", built.query.Encode())
	}
}

func TestNoURLEncodedFieldsSendNoBody(t *testing.T) {
	built, err := newRequest(&Operation{ID: "update", Method: "PATCH", Path: "/items"}, Input{Params: &formParams{}})
	if err != nil {
		t.Fatal(err)
	}
	if built.body != nil || built.contentType != "" {
		t.Errorf("sent %q as %q", built.body, built.contentType)
	}
}

type mixedParams struct {
	Title *string `urlencoded:"title"`
	Image []byte  `form:"image"`
}

func TestURLEncodedAndMultipartFieldsAreRejected(t *testing.T) {
	title := "a"
	params := &mixedParams{Title: &title, Image: []byte("png")}
	if _, err := newRequest(&Operation{ID: "update", Method: "PUT", Path: "/items"}, Input{Params: params}); err == nil {
		t.Fatal("expected an error")
	}
}

func TestDotAndEmptyPathValuesAreRejected(t *testing.T) {
	operation := &Operation{ID: "get", Method: "GET", Path: "/items/{id}", PathParams: []string{"id"}}
	for _, value := range []string{"", ".", ".."} {
		if _, err := newRequest(operation, Input{Path: []any{value}}); err == nil {
			t.Errorf("%q was accepted", value)
		}
	}
	built, err := newRequest(operation, Input{Path: []any{"a.b"}})
	if err != nil {
		t.Fatal(err)
	}
	if built.path != "/items/a.b" {
		t.Errorf("path is %q", built.path)
	}
}

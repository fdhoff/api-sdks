package runtime

import (
	"bytes"
	"context"
	"errors"
	"io"
)

// Download is a binary response. Body streams the bytes as they arrive, unchanged, until the
// attempt's timeout, which keeps running while it is read. Reading past it fails with a timeout
// [Error], and a connection that drops fails with a connection one. The caller must close Body.
type Download struct {
	// ContentType is the response's Content-Type, empty if it has none.
	ContentType string
	Body        io.ReadCloser
}

// downloadBody ends the attempt when it is closed, and reports read failures as an [Error].
type downloadBody struct {
	body      io.ReadCloser
	cancel    context.CancelFunc
	ctx       context.Context
	attempt   context.Context
	transport *Transport
}

func (d *downloadBody) Read(buffer []byte) (int, error) {
	read, err := d.body.Read(buffer)
	if err != nil && !errors.Is(err, io.EOF) {
		return read, d.transport.translate(d.ctx, d.attempt, err)
	}
	return read, err
}

func (d *downloadBody) Close() error {
	err := d.body.Close()
	d.cancel()
	return err
}

// CallDownload sends an operation whose success body is bytes and returns it as a [Download].
// Failures before it is returned are retried as for any call; nothing is retried after.
func CallDownload(ctx context.Context, t *Transport, operation *Operation, input Input) (*Download, error) {
	built, err := newRequest(operation, input)
	if err != nil {
		return nil, err
	}
	answer, err := t.fetch(ctx, built)
	if err != nil {
		return nil, err
	}
	body := answer.stream
	if body == nil {
		body = io.NopCloser(bytes.NewReader(answer.body))
	}
	return &Download{ContentType: answer.header.Get("Content-Type"), Body: body}, nil
}

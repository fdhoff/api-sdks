package multihost

import (
	"context"
	"iter"
)

// Seq is the iterator type a package's client defines.
type Seq[T any] = iter.Seq2[T, error]

func use(ctx context.Context, resources Resources) error {
	tenant := "t1"
	verbose := true
	if _, err := resources.Widgets.Get(ctx, "w1", &WidgetsGetParams{Verbose: &verbose}); err != nil {
		return err
	}
	if _, err := resources.Uploads.List(ctx, nil); err != nil {
		return err
	}
	_, err := resources.Uploads.List(ctx, &UploadsListParams{XTenantId: &tenant})
	return err
}

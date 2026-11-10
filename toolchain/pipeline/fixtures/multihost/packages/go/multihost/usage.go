package multihost

import (
	"context"
	"iter"
	"time"

	"github.com/fdhoff/api-sdks/toolchain/pipeline/fixtures/multihost/packages/go/internal/runtime"
)

// Seq, Download and WaitOptions are types a package's client defines.
type Seq[T any] = iter.Seq2[T, error]

type Download = runtime.Download

type WaitOptions = runtime.WaitOptions

func wait(ctx context.Context, resources Resources) (*ImportStatus, error) {
	return resources.Imports.Wait(ctx, 7, &WaitOptions{Interval: time.Second, Timeout: time.Minute})
}

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

func pages(ctx context.Context, resources Resources) ([]Part, []Bin, error) {
	var parts []Part
	limit := int64(2)
	for part, err := range resources.Parts.Iter(ctx, &PartsListParams{Limit: &limit}) {
		if err != nil {
			return nil, nil, err
		}
		parts = append(parts, part)
	}
	var bins []Bin
	for bin, err := range resources.Bins.Iter(ctx, nil) {
		if err != nil {
			return nil, nil, err
		}
		bins = append(bins, bin)
	}
	return parts, bins, nil
}

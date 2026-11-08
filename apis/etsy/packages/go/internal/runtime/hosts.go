package runtime

import (
	"fmt"
	"maps"
	"slices"
	"strings"
)

// SelectHosts returns the host map to send requests with: hosts when it is not empty, or else the
// named environment's. A caller's own hosts must name exactly the host keys the environments use.
func SelectHosts(environments map[string]map[string]string, environment string, hosts map[string]string) (map[string]string, error) {
	if len(hosts) == 0 {
		chosen, found := environments[environment]
		if !found {
			names := slices.Sorted(maps.Keys(environments))
			return nil, fmt.Errorf("unknown environment %q; expected one of: %s", environment, strings.Join(names, ", "))
		}
		return maps.Clone(chosen), nil
	}
	keys := map[string]bool{}
	for _, environmentHosts := range environments {
		for key := range environmentHosts {
			keys[key] = true
		}
	}
	var missing, unknown []string
	for key := range keys {
		if _, found := hosts[key]; !found {
			missing = append(missing, key)
		}
	}
	for key := range hosts {
		if !keys[key] {
			unknown = append(unknown, key)
		}
	}
	if len(missing) > 0 {
		slices.Sort(missing)
		return nil, fmt.Errorf("hosts lacks: %s", strings.Join(missing, ", "))
	}
	if len(unknown) > 0 {
		slices.Sort(unknown)
		return nil, fmt.Errorf("hosts has unknown keys: %s", strings.Join(unknown, ", "))
	}
	selected := make(map[string]string, len(hosts))
	for key, base := range hosts {
		selected[key] = strings.TrimRight(base, "/")
	}
	return selected, nil
}

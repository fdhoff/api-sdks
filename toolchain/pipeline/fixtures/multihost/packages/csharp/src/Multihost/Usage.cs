using Multihost.Models;

namespace Multihost;

internal static class Usage
{
    internal static async Task<(Widget, Uploads, Uploads)> UseAsync(ClientResources resources) =>
        (await resources.Widgets.GetAsync("w1", verbose: true),
         await resources.Uploads.ListAsync(),
         await resources.Uploads.ListAsync(xTenantId: "t1"));

    internal static Task<ImportStatus> WaitAsync(ClientResources resources, CancellationToken cancellationToken) =>
        resources.Imports.WaitAsync(7, TimeSpan.FromSeconds(1), TimeSpan.FromMinutes(1), cancellationToken);
}

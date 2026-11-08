using Multihost.Models;

namespace Multihost;

internal static class Usage
{
    internal static async Task<(Widget, Uploads, Uploads)> UseAsync(ClientResources resources) =>
        (await resources.Widgets.GetAsync("w1", verbose: true),
         await resources.Uploads.ListAsync(),
         await resources.Uploads.ListAsync(xTenantId: "t1"));
}

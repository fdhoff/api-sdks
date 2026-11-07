using System.Net;
using System.Net.Sockets;
using System.Text;
using Microsoft.Extensions.DependencyInjection;
using Xunit;

namespace BackMarketSeller.Tests;

public sealed class ConnectionTests
{
    private const string Token = "synthetic-token";

    [Fact]
    public async Task WritesReuseTheConnectionButADroppedOneIsNotResent()
    {
        await using var server = new LoopbackServer(Ok("""{"order_id": 1}"""), Ok("{}"), null);
        using var client = new BackMarketClient(Token, Options(server.Url));

        await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);
        await client.Buyback.ValidateOrderAsync("EXAMPLE-1", TestContext.Current.CancellationToken);
        await Assert.ThrowsAsync<ApiConnectionException>(() => client.Buyback.ValidateOrderAsync("EXAMPLE-2", TestContext.Current.CancellationToken));

        Assert.Equal([(1, "GET"), (1, "PUT"), (1, "PUT")], server.Requests.Select(request => (request.Connection, request.Method)));
    }

    [Fact]
    public async Task AnHttpClientPassedInIsUsedAsItIsAndLeftOpen()
    {
        await using var server = new LoopbackServer(Ok("{}"), Ok("{}"));
        using var http = new HttpClient();
        var timeout = http.Timeout;

        using (var client = new BackMarketClient(Token, Options(server.Url), http))
        {
            await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);
        }
        using var after = await http.GetAsync(server.Url, TestContext.Current.CancellationToken);

        Assert.Contains($"Authorization: Basic {Token}\r\n", server.Requests[0].Head);
        Assert.DoesNotContain("Authorization", server.Requests[1].Head);
        Assert.Empty(http.DefaultRequestHeaders);
        Assert.Equal(timeout, http.Timeout);
    }

    [Fact]
    public void AnHttpClientAndAHandlerCannotBothBeSet()
    {
        using var http = new HttpClient();
        using var handler = new HttpClientHandler();
        var options = new BackMarketClientOptions { UserAgent = "BM-A-B;a@example.com", Locale = "fr-fr", Region = Region.EU, HttpHandler = handler };

        Assert.Throws<ArgumentException>(() => new BackMarketClient(Token, options, http));
        Assert.Throws<ArgumentException>(() => new ServiceCollection().AddBackMarketSeller(Token, options));
    }

    [Fact]
    public async Task TheHttpClientFactoryUsesTheClientsOwnHandler()
    {
        await using var server = new LoopbackServer(Ok("""{"order_id": 1}"""), "HTTP/1.1 302 Found\r\nLocation: /ws/orders/2\r\nContent-Length: 0\r\n\r\n");
        var services = new ServiceCollection();
        services.AddBackMarketSeller(Token, Options(server.Url));
        await using var provider = services.BuildServiceProvider();
        var client = provider.GetRequiredService<BackMarketClient>();

        var order = await client.Orders.GetAsync(1, TestContext.Current.CancellationToken);
        await Assert.ThrowsAnyAsync<ApiException>(() => client.Orders.GetAsync(1, TestContext.Current.CancellationToken));

        Assert.Equal(1, order.OrderId);
        Assert.Contains($"Authorization: Basic {Token}\r\n", server.Requests[0].Head);
        Assert.Equal(2, server.Requests.Count);
    }

    private static BackMarketClientOptions Options(Uri url) => new()
    {
        UserAgent = "BM-Example-Tests;tests@example.com",
        Locale = "fr-fr",
        BaseUrl = url,
        MaxRetries = 0,
    };

    private static string Ok(string json) =>
        $"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {Encoding.UTF8.GetByteCount(json)}\r\n\r\n{json}";

    /// <summary>Answers each request in turn with a raw response, or with null by closing the connection unanswered.</summary>
    private sealed class LoopbackServer : IAsyncDisposable
    {
        private readonly TcpListener listener = new(IPAddress.Loopback, 0);
        private readonly string?[] responses;
        private readonly Task accepting;
        private readonly List<Task> serving = [];

        public LoopbackServer(params string?[] responses)
        {
            this.responses = responses;
            listener.Start();
            accepting = AcceptAsync();
        }

        public Uri Url => new($"http://127.0.0.1:{((IPEndPoint)listener.LocalEndpoint).Port}/");

        public List<Received> Requests { get; } = [];

        public async ValueTask DisposeAsync()
        {
            listener.Stop();
            await accepting.ConfigureAwait(false);
            await Task.WhenAll(serving).ConfigureAwait(false);
        }

        private async Task AcceptAsync()
        {
            for (var connection = 1; ; connection++)
            {
                TcpClient socket;
                try
                {
                    socket = await listener.AcceptTcpClientAsync().ConfigureAwait(false);
                }
                catch (Exception error) when (error is SocketException or ObjectDisposedException)
                {
                    return;
                }
                serving.Add(ServeAsync(socket, connection));
            }
        }

        private async Task ServeAsync(TcpClient socket, int connection)
        {
            using (socket)
            {
                var stream = socket.GetStream();
                while (await ReadHeadAsync(stream).ConfigureAwait(false) is { } head)
                {
                    var length = head.Split("\r\n")
                        .Where(line => line.StartsWith("Content-Length:", StringComparison.OrdinalIgnoreCase))
                        .Select(line => int.Parse(line["Content-Length:".Length..].Trim(), System.Globalization.CultureInfo.InvariantCulture))
                        .FirstOrDefault();
                    await stream.ReadExactlyAsync(new byte[length]).ConfigureAwait(false);
                    int index;
                    lock (Requests)
                    {
                        Requests.Add(new Received(connection, head[..head.IndexOf(' ')], head));
                        index = Requests.Count - 1;
                    }
                    if (index >= responses.Length || responses[index] is not { } response)
                    {
                        return;
                    }
                    await stream.WriteAsync(Encoding.UTF8.GetBytes(response)).ConfigureAwait(false);
                }
            }
        }

        private static async Task<string?> ReadHeadAsync(NetworkStream stream)
        {
            var head = new List<byte>();
            var one = new byte[1];
            while (head.Count < 4 || !head.TakeLast(4).SequenceEqual("\r\n\r\n"u8.ToArray()))
            {
                try
                {
                    if (await stream.ReadAsync(one).ConfigureAwait(false) == 0)
                    {
                        return null;
                    }
                }
                catch (IOException)
                {
                    return null;
                }
                head.Add(one[0]);
            }
            return Encoding.ASCII.GetString([.. head]);
        }
    }

    private sealed record Received(int Connection, string Method, string Head);
}

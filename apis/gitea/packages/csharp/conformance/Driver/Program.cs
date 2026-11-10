// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
//
// The client adds /api/v1 to the instance URL, while the mock cases name each path as the spec declares it, because
// the mock serves them without the prefix. So the driver's handler removes the prefix on the way out, and a request
// without it goes out unchanged and fails the case's path check. With --live, for the live scenarios against a
// disposable Gitea container, every request goes out unchanged. See apis/gitea/docs/live.md.
using System.Reflection;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using GiteaRest;
using GiteaRest.Models;
using GiteaRest.Runtime;
using Microsoft.Extensions.Logging;

var live = args.Contains("--live");
using var handler = live ? (HttpMessageHandler)Transport.CreateHandler() : new StripApiPath(Transport.CreateHandler());
var output = new StreamWriter(Console.OpenStandardOutput(), new UTF8Encoding(false)) { AutoFlush = true };
string? line;
while ((line = Console.ReadLine()) is not null)
{
    using var message = JsonDocument.Parse(line);
    output.WriteLine(await Driver.RunAsync(message.RootElement, handler));
}

internal static class Driver
{
    private static readonly MethodInfo CollectMethod = typeof(Driver).GetMethod(nameof(CollectAsync), BindingFlags.NonPublic | BindingFlags.Static)!;

    private static readonly JsonSerializerOptions Lenient = new() { NumberHandling = System.Text.Json.Serialization.JsonNumberHandling.AllowReadingFromString };

    public static async Task<string> RunAsync(JsonElement message, HttpMessageHandler handler)
    {
        var settings = message.GetProperty("client");
        var request = message.GetProperty("request");
        var logs = new Capture();
        using var client = new GiteaClient(settings.GetProperty("base_url").GetString()!, Credentials(settings), Options(settings, logs, handler));
        var reply = new JsonObject();
        try
        {
            reply["result"] = await CallAsync(client, request);
        }
        catch (ApiException error)
        {
            reply["error"] = ErrorOutput(error);
        }
        reply["logs"] = new JsonArray([.. logs.Lines.Select(entry => (JsonNode)entry)]);
        return reply.ToJsonString();
    }

    private static string? Text(JsonElement settings, string name) =>
        settings.TryGetProperty(name, out var value) && value.ValueKind == JsonValueKind.String ? value.GetString() : null;

    /// <summary>A case that sets <c>username</c> uses Basic, with the one-time password unless it is null. Otherwise the token.</summary>
    private static GiteaCredentials Credentials(JsonElement settings) =>
        Text(settings, "username") is { } username
            ? GiteaCredentials.Basic(username, Text(settings, "password")!, Text(settings, "otp"))
            : GiteaCredentials.Token(Text(settings, "token")!);

    private static async Task<JsonNode?> CallAsync(GiteaClient client, JsonElement request)
    {
        var operationId = request.GetProperty("operation").GetString();
        var operation = ClientResources.Operations.Single(item => item.Id == operationId);
        var paginate = request.TryGetProperty("paginate", out var flag) && flag.GetBoolean();
        var resource = typeof(GiteaClient).GetProperty(operation.Resource)!.GetValue(client)!;
        var method = resource.GetType().GetMethod(paginate ? operation.Iterator! : operation.Name)!;
        var returned = method.Invoke(resource, Arguments(method, operation, request));
        if (paginate)
        {
            var item = method.ReturnType.GetGenericArguments()[0];
            var items = await (Task<List<object?>>)CollectMethod.MakeGenericMethod(item).Invoke(null, [returned])!;
            return JsonSerializer.SerializeToNode(items);
        }
        var task = (Task)returned!;
        await task;
        var result = method.ReturnType == typeof(Task) ? null : task.GetType().GetProperty("Result")!.GetValue(task);
        return result switch
        {
            null => null,
            Download download => await DownloadOutputAsync(download),
            _ => JsonSerializer.SerializeToNode(result, result.GetType()),
        };
    }

    private static TimeSpan? Milliseconds(JsonElement settings, string name) =>
        settings.TryGetProperty(name, out var value) ? TimeSpan.FromMilliseconds(value.GetDouble()) : null;

    private static GiteaClientOptions Options(JsonElement settings, Capture logs, HttpMessageHandler handler)
    {
        var defaults = new GiteaClientOptions();
        return new GiteaClientOptions
        {
            Sudo = Text(settings, "sudo"),
            UserAgent = Text(settings, "user_agent"),
            Timeout = Milliseconds(settings, "timeout_ms") ?? defaults.Timeout,
            MaxRetries = settings.TryGetProperty("max_retries", out var retries) ? retries.GetInt32() : defaults.MaxRetries,
            RetryBaseDelay = Milliseconds(settings, "retry_base_delay_ms") ?? defaults.RetryBaseDelay,
            RateLimitWait = Milliseconds(settings, "rate_limit_wait_ms") ?? defaults.RateLimitWait,
            MaxRetryWait = Milliseconds(settings, "max_retry_wait_ms") ?? defaults.MaxRetryWait,
            Logger = logs,
            HttpHandler = handler,
        };
    }

    private static object?[] Arguments(MethodInfo method, Operation operation, JsonElement request)
    {
        var values = new Dictionary<string, JsonElement>();
        foreach (var section in new[] { "params", "multipart" })
        {
            if (!request.TryGetProperty(section, out var fields))
            {
                continue;
            }
            foreach (var field in fields.EnumerateObject())
            {
                values[operation.Params.Single(param => param.Wire == field.Name).Name] = field.Value;
            }
        }
        if (request.TryGetProperty("body", out var body))
        {
            values["body"] = body;
        }
        return [.. method.GetParameters().Select(parameter =>
            parameter.ParameterType == typeof(CancellationToken) ? CancellationToken.None
            : values.TryGetValue(parameter.Name!, out var value) ? Convert(value, parameter.ParameterType, parameter.Name!)
            : parameter.DefaultValue)];
    }

    private static object? Convert(JsonElement value, Type type, string name)
    {
        var target = Nullable.GetUnderlyingType(type) ?? type;
        if (target == typeof(string) && value.ValueKind != JsonValueKind.String)
        {
            return value.GetRawText();
        }
        if (target == typeof(UploadFile))
        {
            return Upload(value, name);
        }
        if (target == typeof(List<UploadFile>))
        {
            return value.ValueKind == JsonValueKind.Array ? value.EnumerateArray().Select(item => Upload(item, name)).ToList() : [Upload(value, name)];
        }
        // A multipart JSON part arrives as its text.
        if (typeof(ApiModel).IsAssignableFrom(target) && value.ValueKind == JsonValueKind.String)
        {
            return JsonSerializer.Deserialize(value.GetString()!, type, Lenient);
        }
        return value.Deserialize(type, Lenient);
    }

    private static UploadFile Upload(JsonElement value, string name)
    {
        var text = value.ValueKind == JsonValueKind.String ? value.GetString()! : value.GetRawText();
        return new UploadFile(name, Encoding.UTF8.GetBytes(text));
    }

    private static async Task<JsonObject> DownloadOutputAsync(Download download)
    {
        await using (download)
        {
            var bytes = await download.ReadAllBytesAsync();
            return new JsonObject { ["content_type"] = download.ContentType, ["base64"] = System.Convert.ToBase64String(bytes) };
        }
    }

    private static JsonObject ErrorOutput(ApiException error)
    {
        var fields = new JsonObject { ["kind"] = error.Kind };
        if (error.Status is { } status)
        {
            fields["status"] = status;
            fields["raw_body"] = error.RawBody ?? string.Empty;
        }
        if (error is HttpException { Detail: { } detail })
        {
            fields["message"] = detail;
        }
        return fields;
    }

    private static async Task<List<object?>> CollectAsync<T>(IAsyncEnumerable<T> items)
    {
        var collected = new List<object?>();
        await foreach (var item in items)
        {
            collected.Add(item);
        }
        return collected;
    }

    private sealed class Capture : ILogger
    {
        public List<string> Lines { get; } = [];

        public IDisposable? BeginScope<TState>(TState state)
            where TState : notnull => null;

        public bool IsEnabled(LogLevel logLevel) => true;

        public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception? exception, Func<TState, Exception?, string> formatter) =>
            Lines.Add(formatter(state, exception));
    }
}

/// <summary>Removes the client's /api/v1 from each request on its way to the mock, which serves the spec's paths without it.</summary>
internal sealed class StripApiPath(HttpMessageHandler inner) : DelegatingHandler(inner)
{
    private const string ApiPath = "/api/v1";

    protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
    {
        var url = request.RequestUri!;
        var path = url.AbsolutePath;
        if (path.StartsWith(ApiPath + "/", StringComparison.Ordinal))
        {
            request.RequestUri = new Uri(url.GetLeftPart(UriPartial.Authority) + path[ApiPath.Length..] + url.Query);
        }
        return base.SendAsync(request, cancellationToken);
    }
}

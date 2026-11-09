// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
using System.Globalization;
using System.Reflection;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using MiraklSeller;
using MiraklSeller.Models;
using MiraklSeller.Runtime;
using Microsoft.Extensions.Logging;

var output = new StreamWriter(Console.OpenStandardOutput(), new UTF8Encoding(false)) { AutoFlush = true };
string? line;
while ((line = Console.ReadLine()) is not null)
{
    using var message = JsonDocument.Parse(line);
    output.WriteLine(await Driver.RunAsync(message.RootElement));
}

internal static class Driver
{
    private static readonly MethodInfo CollectMethod = typeof(Driver).GetMethod(nameof(CollectAsync), BindingFlags.NonPublic | BindingFlags.Static)!;

    private static readonly JsonSerializerOptions Lenient = new() { NumberHandling = System.Text.Json.Serialization.JsonNumberHandling.AllowReadingFromString };

    public static async Task<string> RunAsync(JsonElement message)
    {
        var settings = message.GetProperty("client");
        var request = message.GetProperty("request");
        var logs = new Capture();
        using var client = new MiraklClient(settings.GetProperty("base_url").GetString()!, settings.GetProperty("token").GetString()!, Options(settings, logs));
        var reply = new JsonObject();
        try
        {
            reply["result"] = request.TryGetProperty("download", out var url)
                ? await DownloadOutputAsync(await client.DownloadUrlAsync(url.GetString()!))
                : await CallAsync(client, settings, request);
        }
        catch (ApiException error)
        {
            reply["error"] = ErrorOutput(error);
        }
        reply["logs"] = new JsonArray([.. logs.Lines.Select(entry => (JsonNode)entry)]);
        return reply.ToJsonString();
    }

    private static async Task<JsonNode?> CallAsync(MiraklClient client, JsonElement settings, JsonElement request)
    {
        var operationId = request.GetProperty("operation").GetString();
        var operation = ClientResources.Operations.Single(item => item.Id == operationId);
        var paginate = request.TryGetProperty("paginate", out var flag) && flag.GetBoolean();
        var wait = request.TryGetProperty("wait", out var waiting) && waiting.GetBoolean();
        var resource = typeof(MiraklClient).GetProperty(operation.Resource)!.GetValue(client)!;
        var method = resource.GetType().GetMethod(paginate ? operation.Iterator! : operation.Name)!;
        if (wait)
        {
            // A job's wait method returns the same status as the operation it polls, which no other wait on the resource does.
            method = resource.GetType().GetMethods().Single(candidate => candidate.Name.StartsWith("WaitFor", StringComparison.Ordinal) && candidate.ReturnType == method.ReturnType);
        }
        var returned = method.Invoke(resource, Arguments(method, operation, request, settings));
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

    private static MiraklClientOptions Options(JsonElement settings, Capture logs)
    {
        string? Text(string name) => settings.TryGetProperty(name, out var value) ? value.GetString() : null;

        var defaults = new MiraklClientOptions();
        long? shopId = settings.TryGetProperty("query_defaults", out var queryDefaults) && queryDefaults.TryGetProperty("shop_id", out var shop)
            ? long.Parse(shop.ValueKind == JsonValueKind.String ? shop.GetString()! : shop.GetRawText(), CultureInfo.InvariantCulture)
            : null;
        return new MiraklClientOptions
        {
            ShopId = shopId,
            UserAgent = Text("user_agent"),
            Timeout = Milliseconds(settings, "timeout_ms") ?? defaults.Timeout,
            MaxRetries = settings.TryGetProperty("max_retries", out var retries) ? retries.GetInt32() : defaults.MaxRetries,
            RetryBaseDelay = Milliseconds(settings, "retry_base_delay_ms") ?? defaults.RetryBaseDelay,
            RateLimitWait = Milliseconds(settings, "rate_limit_wait_ms") ?? defaults.RateLimitWait,
            MaxRetryWait = Milliseconds(settings, "max_retry_wait_ms") ?? defaults.MaxRetryWait,
            Logger = logs,
        };
    }

    private static object?[] Arguments(MethodInfo method, Operation operation, JsonElement request, JsonElement settings)
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
            : parameter.ParameterType == typeof(TimeSpan?) && parameter.Name == "interval" ? Milliseconds(settings, "poll_interval_ms")
            : parameter.ParameterType == typeof(TimeSpan?) && parameter.Name == "timeout" ? Milliseconds(settings, "poll_timeout_ms")
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
        }
        if (error.RawBody is { } raw)
        {
            fields["raw_body"] = raw;
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

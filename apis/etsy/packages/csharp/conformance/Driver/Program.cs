// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
using System.Reflection;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using EtsySeller;
using EtsySeller.Runtime;
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

    public static async Task<string> RunAsync(JsonElement message)
    {
        var settings = message.GetProperty("client");
        var request = message.GetProperty("request");
        var logs = new Capture();
        using var client = new EtsyClient(settings.GetProperty("api_key").GetString()!, settings.GetProperty("shared_secret").GetString()!, Options(settings, logs));
        var operationId = request.GetProperty("operation").GetString();
        var operation = ClientResources.Operations.Single(item => item.Id == operationId);
        var paginate = request.TryGetProperty("paginate", out var flag) && flag.GetBoolean();
        var resource = typeof(EtsyClient).GetProperty(operation.Resource)!.GetValue(client)!;
        var method = resource.GetType().GetMethod(paginate ? operation.Iterator! : operation.Name)!;
        var reply = new JsonObject();
        try
        {
            var returned = method.Invoke(resource, Arguments(method, operation, request));
            object? result;
            if (paginate)
            {
                var item = method.ReturnType.GetGenericArguments()[0];
                result = await (Task<List<object?>>)CollectMethod.MakeGenericMethod(item).Invoke(null, [returned])!;
            }
            else
            {
                var task = (Task)returned!;
                await task;
                result = method.ReturnType == typeof(Task) ? null : task.GetType().GetProperty("Result")!.GetValue(task);
            }
            reply["result"] = result is null ? null : JsonSerializer.SerializeToNode(result, result.GetType());
        }
        catch (ApiException error)
        {
            reply["error"] = ErrorOutput(error);
        }
        reply["logs"] = new JsonArray([.. logs.Lines.Select(entry => (JsonNode)entry)]);
        return reply.ToJsonString();
    }

    private static EtsyClientOptions Options(JsonElement settings, Capture logs)
    {
        TimeSpan? Milliseconds(string name) =>
            settings.TryGetProperty(name, out var value) ? TimeSpan.FromMilliseconds(value.GetDouble()) : null;

        var defaults = new EtsyClientOptions();
        return new EtsyClientOptions
        {
            BaseUrl = new Uri(settings.GetProperty("base_url").GetString()!),
            AccessToken = settings.GetProperty("token").GetString(),
            UserAgent = settings.TryGetProperty("user_agent", out var agent) ? agent.GetString() : null,
            Timeout = Milliseconds("timeout_ms") ?? defaults.Timeout,
            MaxRetries = settings.TryGetProperty("max_retries", out var retries) ? retries.GetInt32() : defaults.MaxRetries,
            RetryBaseDelay = Milliseconds("retry_base_delay_ms") ?? defaults.RetryBaseDelay,
            RateLimitWait = Milliseconds("rate_limit_wait_ms") ?? defaults.RateLimitWait,
            MaxRetryWait = Milliseconds("max_retry_wait_ms") ?? defaults.MaxRetryWait,
            Logger = logs,
        };
    }

    /// <summary>A form body's fields are method arguments, like path and query parameters.</summary>
    private static object?[] Arguments(MethodInfo method, Operation operation, JsonElement request)
    {
        var form = operation.Params.Any(param => param.Location is ParamLocation.Form or ParamLocation.Urlencoded);
        var values = new Dictionary<string, JsonElement>();
        foreach (var section in form ? new[] { "params", "multipart", "body" } : ["params", "multipart"])
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
        if (!form && request.TryGetProperty("body", out var body))
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
        if (target == typeof(UploadFile) && value.ValueKind == JsonValueKind.String)
        {
            return new UploadFile(name, Encoding.UTF8.GetBytes(value.GetString()!));
        }
        return value.Deserialize(type);
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

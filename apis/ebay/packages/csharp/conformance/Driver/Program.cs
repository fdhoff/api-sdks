// Conformance driver: reads cases as JSON lines and calls the public client. See the runner's README.
using System.Reflection;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using EbaySell;
using EbaySell.Runtime;
using Microsoft.Extensions.Logging;
using Org.BouncyCastle.Crypto.Generators;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Pkcs;
using Org.BouncyCastle.Security;

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

    /// <summary>Each contract's name in the cases, and the client property that holds it.</summary>
    private static readonly Dictionary<string, PropertyInfo> Contracts = typeof(EbayClient).GetProperties()
        .Select(property => (property, field: property.PropertyType.GetField("Contract", BindingFlags.NonPublic | BindingFlags.Static)))
        .Where(pair => pair.field is not null)
        .ToDictionary(pair => (string)pair.field!.GetValue(null)!, pair => pair.property);

    /// <summary>Generated per run, never stored: the cases check the signature's shape and digest, not the key.</summary>
    private static readonly string PrivateKey = CreatePrivateKey();

    public static async Task<string> RunAsync(JsonElement message)
    {
        var settings = message.GetProperty("client");
        var request = message.GetProperty("request");
        var logs = new Capture();
        using var client = new EbayClient(Options(settings, logs));
        var (contract, operationId) = Split(request.GetProperty("operation").GetString()!);
        var api = Contracts[contract].GetValue(client)!;
        var operations = (Operation[])api.GetType().GetField("Operations", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null)!;
        var operation = operations.Single(item => item.Id == operationId);
        var paginate = request.TryGetProperty("paginate", out var flag) && flag.GetBoolean();
        var resource = api.GetType().GetProperty(operation.Resource)!.GetValue(api)!;
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

    private static (string, string) Split(string name)
    {
        var dot = name.IndexOf('.', StringComparison.Ordinal);
        return (name[..dot], name[(dot + 1)..]);
    }

    private static EbayClientOptions Options(JsonElement settings, Capture logs)
    {
        TimeSpan? Milliseconds(string name) =>
            settings.TryGetProperty(name, out var value) ? TimeSpan.FromMilliseconds(value.GetDouble()) : null;
        string? Text(string name) => settings.TryGetProperty(name, out var value) ? value.GetString() : null;
        string? Default(string name) =>
            settings.TryGetProperty("header_defaults", out var defaults) && defaults.TryGetProperty(name, out var value) ? value.GetString() : null;

        var defaults = new EbayClientOptions();
        var environment = Text("environment");
        return new EbayClientOptions
        {
            Environment = environment ?? EbayClient.Production,
            Hosts = Hosts(Text("base_url")!, environment),
            AppToken = Text("app_token"),
            UserToken = Text("user_token"),
            MarketplaceId = Default("X-EBAY-C-MARKETPLACE-ID"),
            ContentLanguage = Default("Content-Language"),
            SigningKey = Text("signature_key") is { } jwe ? new EbaySigningKey(PrivateKey, jwe) : null,
            UserAgent = Text("user_agent"),
            Timeout = Milliseconds("timeout_ms") ?? defaults.Timeout,
            MaxRetries = settings.TryGetProperty("max_retries", out var retries) ? retries.GetInt32() : defaults.MaxRetries,
            RetryBaseDelay = Milliseconds("retry_base_delay_ms") ?? defaults.RetryBaseDelay,
            RateLimitWait = Milliseconds("rate_limit_wait_ms") ?? defaults.RateLimitWait,
            MaxRetryWait = Milliseconds("max_retry_wait_ms") ?? defaults.MaxRetryWait,
            Logger = logs,
        };
    }

    /// <summary>Each host key's harness prefix: the key itself, or with an environment the hostname that environment gives the key.</summary>
    private static Dictionary<string, string> Hosts(string baseUrl, string? environment) =>
        EbayClient.Environments[environment ?? EbayClient.Production].ToDictionary(
            pair => pair.Key,
            pair => $"{baseUrl.TrimEnd('/')}/_host/{(environment is null ? pair.Key : new Uri(pair.Value).Host)}");

    /// <summary>A form body's fields are method arguments, like path, query and header parameters.</summary>
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
        if (target == typeof(UploadFile))
        {
            var text = value.ValueKind == JsonValueKind.String ? value.GetString()! : value.GetRawText();
            return new UploadFile(name, Encoding.UTF8.GetBytes(text));
        }
        return value.Deserialize(type, Lenient);
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
        if (long.TryParse(error.Code, out var code))
        {
            fields["code"] = code;
        }
        return fields;
    }

    private static string CreatePrivateKey()
    {
        var generator = new Ed25519KeyPairGenerator();
        generator.Init(new Ed25519KeyGenerationParameters(new SecureRandom()));
        var info = PrivateKeyInfoFactory.CreatePrivateKeyInfo(generator.GenerateKeyPair().Private);
        var body = System.Convert.ToBase64String(info.GetEncoded());
        return EbaySigningKey.Pem(body);
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

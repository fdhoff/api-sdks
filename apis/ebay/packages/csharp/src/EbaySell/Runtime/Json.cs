using System.Reflection;
using System.Text.Json;
using System.Text.Json.Serialization;
using EbaySell.Models;

namespace EbaySell.Runtime;

internal static class Json
{
    public static readonly JsonSerializerOptions Options = new()
    {
        DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
    };

    public static JsonElement? TryParse(string text)
    {
        try
        {
            using var document = JsonDocument.Parse(text);
            return document.RootElement.Clone();
        }
        catch (JsonException)
        {
            return null;
        }
    }

    /// <summary>Text for a URL or a form field: strings as they are, anything else as its JSON value.</summary>
    public static string Text(object value)
    {
        if (value is string text)
        {
            return text;
        }
        var element = JsonSerializer.SerializeToElement(value, value.GetType(), Options);
        return element.ValueKind == JsonValueKind.String ? element.GetString()! : element.GetRawText();
    }

    public static T Read<T>(JsonElement element, int? status, string raw)
    {
        if (element.ValueKind == JsonValueKind.Null)
        {
            return Empty<T>();
        }
        try
        {
            return element.Deserialize<T>(Options)!;
        }
        catch (JsonException error)
        {
            throw new ApiDecodeException($"The response is not a {typeof(T).Name}", error) { Status = status, RawBody = raw };
        }
    }

    /// <summary>A JSON <c>null</c> reads as an empty value.</summary>
    public static T Empty<T>()
    {
        if (typeof(T) == typeof(string))
        {
            return (T)(object)string.Empty;
        }
        return typeof(T).GetConstructor(Type.EmptyTypes) is null ? default! : Activator.CreateInstance<T>();
    }
}

/// <summary>Reads a model tolerantly and writes it back with its extra fields.</summary>
internal sealed class ApiModelConverter<T> : JsonConverter<T>
    where T : ApiModel, new()
{
    private static readonly Dictionary<string, PropertyInfo> Fields = typeof(T)
        .GetProperties()
        .Select(property => (Name: property.GetCustomAttribute<JsonPropertyNameAttribute>()?.Name, Property: property))
        .Where(field => field.Name is not null)
        .ToDictionary(field => field.Name!, field => field.Property);

    public override T Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        using var document = JsonDocument.ParseValue(ref reader);
        if (document.RootElement.ValueKind != JsonValueKind.Object)
        {
            throw new JsonException($"{typeof(T).Name} must be a JSON object");
        }
        var model = new T();
        foreach (var member in document.RootElement.EnumerateObject())
        {
            var raw = member.Value.Clone();
            var known = Fields.TryGetValue(member.Name, out var field);
            object? value = null;
            if (known && raw.ValueKind != JsonValueKind.Null && TryRead(raw, field!.PropertyType, options, out value))
            {
                model.Extra.Remove(member.Name);
            }
            else
            {
                model.Extra[member.Name] = raw;
            }
            field?.SetValue(model, value);
        }
        return model;
    }

    public override void Write(Utf8JsonWriter writer, T value, JsonSerializerOptions options)
    {
        writer.WriteStartObject();
        var written = new HashSet<string>();
        foreach (var (name, field) in Fields)
        {
            var item = field.GetValue(value);
            if (item is null)
            {
                continue;
            }
            writer.WritePropertyName(name);
            JsonSerializer.Serialize(writer, item, field.PropertyType, options);
            written.Add(name);
        }
        foreach (var (name, raw) in value.Extra)
        {
            if (written.Contains(name))
            {
                continue;
            }
            writer.WritePropertyName(name);
            raw.WriteTo(writer);
        }
        writer.WriteEndObject();
    }

    private static bool TryRead(JsonElement raw, Type type, JsonSerializerOptions options, out object? value)
    {
        try
        {
            value = raw.Deserialize(type, options);
            return true;
        }
        catch (JsonException)
        {
            value = null;
            return false;
        }
    }
}

/// <summary>Reads and writes an enum by its API value only, never by its number.</summary>
internal sealed class ApiEnumConverter<T>() : JsonStringEnumConverter<T>(namingPolicy: null, allowIntegerValues: false)
    where T : struct, Enum;

using System.Text.Json;
using System.Text.Json.Serialization;

namespace EtsySeller.Models;

/// <summary>
/// Base of every generated model.
/// </summary>
/// <remarks>
/// Responses are read tolerantly, because nothing has been confirmed against the live API. A value that does not
/// fit its property leaves the property null and is kept in <see cref="Extra"/>, along with unknown fields and
/// nulls. Serializing a model writes its set properties, then <see cref="Extra"/>.
/// </remarks>
public abstract class ApiModel
{
    /// <summary>Fields this version does not declare, values that did not fit their property, and nulls, by API name.</summary>
    [JsonIgnore]
    public IDictionary<string, JsonElement> Extra { get; } = new Dictionary<string, JsonElement>();
}

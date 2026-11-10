namespace GiteaRest;

/// <summary>A file to upload in a multipart request.</summary>
/// <param name="FileName">The name sent with the file.</param>
/// <param name="Content">The file's bytes.</param>
public sealed record UploadFile(string FileName, byte[] Content);

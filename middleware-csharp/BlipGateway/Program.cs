var builder = WebApplication.CreateBuilder(args);

// 1. Adicionamos o serviço de HttpClient para podermos "ligar" para o Python
builder.Services.AddHttpClient();

var app = builder.Build();

// Rota de teste para garantir que o Middleware está vivo
app.MapGet("/", () => new { status = "Middleware .NET is running!" });

// 2. A nossa rota principal que vai chamar o Python
app.MapGet("/ask-ai", async (string question, HttpClient client) =>
{
    // O endereço onde o teu servidor Python está a correr
    var pythonUrl = $"http://127.0.0.1:8000/ask?question={question}";

    try 
    {
        // O C# envia a pergunta para o Python
        var response = await client.GetFromJsonAsync<object>(pythonUrl);
        
        // O C# recebe a resposta e devolve-a para quem perguntou (ex: o teu futuro Front-end)
        return Results.Ok(new { 
            source = "Middleware .NET",
            data = response 
        });
    }
    catch (Exception ex)
    {
        return Results.Problem($"Error calling AI Engine: {ex.Message}");
    }
});

app.Run();
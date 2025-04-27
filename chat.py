import httpx

GEMINI_API_KEY = "sua-chave-da-api-aqui"

async def perguntar_gemini(pergunta: str):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
            "parts": [{"text": pergunta}]
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        resposta = response.json()
        try:
            return resposta["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            return "Erro ao consultar IA."

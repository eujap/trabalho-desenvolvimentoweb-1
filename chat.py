import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def perguntar_gemini(pergunta: str):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {
                    "parts": [{"text": pergunta}]
                }
            ]
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()  # Vai mostrar erro HTTP se houver
            resposta = response.json()
            return resposta["candidates"][0]["content"]["parts"][0]["text"]
    except httpx.HTTPStatusError as e:
        return f"Erro HTTP: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Erro geral: {str(e)}"

import ollama

MODEL_NAME = "gemma2:2b"


def get_healthcare_response(user_query: str) -> str:
    system_prompt = """
You are an AI Healthcare Assistant.

Rules:
- Answer only general healthcare questions.
- Never diagnose diseases.
- Never prescribe medicines.
- Recommend consulting a healthcare professional when appropriate.
- Keep answers short and easy to understand.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ],
    )

    return response["message"]["content"]
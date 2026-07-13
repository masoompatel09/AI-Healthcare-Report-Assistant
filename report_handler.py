import ollama

MODEL_NAME = "gemma2:2b"


def explain_report(report_summary: str) -> str:
    """
    Converts the raw report summary into a patient-friendly explanation.
    """

    system_prompt = """
You are an AI Healthcare Assistant.

Your task is to explain a patient's medical report summary in simple language.

Rules:
- Use easy English.
- Explain medical terms if present.
- Do not invent information.
- Do not diagnose diseases.
- Do not prescribe medicines.
- Recommend consulting a doctor if necessary.
- Keep the explanation under 150 words.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": report_summary
            }
        ]
    )

    return response["message"]["content"]
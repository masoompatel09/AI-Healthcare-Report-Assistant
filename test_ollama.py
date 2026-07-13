import ollama

response = ollama.chat(
    model="gemma2:2b",
    messages=[
        {
            "role": "user",
            "content": "What is diabetes?"
        }
    ]
)

print(response["message"]["content"])
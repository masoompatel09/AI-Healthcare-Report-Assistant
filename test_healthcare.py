from healthcare import get_healthcare_response

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = get_healthcare_response(question)
    print("\nAssistant:", answer)
from intent_classifier import classify_intent

test_cases = [

    # Report Requests
    "Show my report",
    "I want my blood report",
    "Open my report",
    "Can I see my report?",
    "Download my health report",
    "Retrieve my report",

    # Healthcare Queries
    "What is diabetes?",
    "Explain blood report",
    "What causes fever?",
    "Explain MRI report",
    "How do doctors prepare reports?",
    "What is hypertension?",

    # Unknown
    "Hello",
    "Hi",
    "Thank you",
    "Good Morning",
    "Bye"
]

for message in test_cases:
    intent = classify_intent(message)
    print(f"{message:<40} --> {intent}")
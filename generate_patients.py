import pandas as pd

patients = [
    {
        "Email ID": "rahul.sharma@gmail.com",
        "Password": "Rahul@123",
        "Report Summary": "Blood pressure is normal. Mild Vitamin D deficiency detected.",
        "Report Link": "https://drive.google.com/file/d/report1/view"
    },
    {
        "Email ID": "priya.patel@gmail.com",
        "Password": "Priya@456",
        "Report Summary": "Mild anemia detected. Iron-rich diet recommended.",
        "Report Link": "https://drive.google.com/file/d/report2/view"
    },
    {
        "Email ID": "aman.verma@gmail.com",
        "Password": "Aman@789",
        "Report Summary": "Elevated cholesterol levels. Lifestyle changes advised.",
        "Report Link": "https://drive.google.com/file/d/report3/view"
    },
    {
        "Email ID": "neha.desai@gmail.com",
        "Password": "Neha@321",
        "Report Summary": "Blood sugar within normal range. Continue healthy diet.",
        "Report Link": "https://drive.google.com/file/d/report4/view"
    },
    {
        "Email ID": "rohit.mehta@gmail.com",
        "Password": "Rohit@654",
        "Report Summary": "Thyroid function normal. No abnormalities detected.",
        "Report Link": "https://drive.google.com/file/d/report5/view"
    },
    {
        "Email ID": "kavya.shah@gmail.com",
        "Password": "Kavya@111",
        "Report Summary": "Calcium level slightly low. Increase dairy intake.",
        "Report Link": "https://drive.google.com/file/d/report6/view"
    },
    {
        "Email ID": "arjun.patel@gmail.com",
        "Password": "Arjun@222",
        "Report Summary": "Liver function tests are normal.",
        "Report Link": "https://drive.google.com/file/d/report7/view"
    },
    {
        "Email ID": "meera.joshi@gmail.com",
        "Password": "Meera@333",
        "Report Summary": "Hemoglobin slightly low. Follow-up after one month.",
        "Report Link": "https://drive.google.com/file/d/report8/view"
    },
    {
        "Email ID": "vivek.kumar@gmail.com",
        "Password": "Vivek@444",
        "Report Summary": "Kidney function normal. Stay hydrated.",
        "Report Link": "https://drive.google.com/file/d/report9/view"
    },
    {
        "Email ID": "isha.modi@gmail.com",
        "Password": "Isha@555",
        "Report Summary": "Overall health parameters are within normal limits.",
        "Report Link": "https://drive.google.com/file/d/report10/view"
    }
]

df = pd.DataFrame(patients)

df.to_excel("patients.xlsx", index=False)

print("patients.xlsx created successfully!")
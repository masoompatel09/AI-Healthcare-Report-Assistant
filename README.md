# How to Run the AI Healthcare Report Assistant 🏥

This guide provides a comprehensive list of commands to set up the environment, configure the AI model, initialize the database, and run the Streamlit application.

---

## 🛠️ Step 1: Set up Ollama & Pull the Model

Ensure that the Ollama app is installed and running on your system, then pull the required **Gemma 2 (2B)** model.

```bash
# Pull the Gemma 2 (2B) model
ollama pull gemma2:2b
```

---

## 📦 Step 2: Create and Activate Virtual Environment

Open your terminal in the project's root directory:

### **On Windows (PowerShell/CMD)**
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

### **On macOS / Linux**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

---

## 📥 Step 3: Install Required Dependencies

Install the necessary Python packages using pip:

```bash
pip install streamlit pandas openpyxl ollama
```

---

## 🗄️ Step 4: Generate/Seed the Patient Database

Create the mock patient Excel spreadsheet (`patients.xlsx`) containing test user accounts and reports:

```bash
python generate_patients.py
```

---

## 🚀 Step 5: Start the Streamlit Application

You can now start the Streamlit web application using the following commands:

### **Standard Command**
```bash
streamlit run app.py
```

### **Windows Launcher Error Bypass**
If you get a launcher error like *"Fatal error in launcher: Unable to create process..."*, run the app directly through python:
```powershell
python -m streamlit run app.py
```

---

## 🔑 Mock Credentials for Testing
When testing the secure patient report access flow, you can use these mock credentials:

| Email ID | Password | Expected Report Summary |
| :--- | :--- | :--- |
| `rahul.sharma@gmail.com` | `Rahul@123` | Blood pressure is normal. Mild Vitamin D deficiency detected. |
| `priya.patel@gmail.com` | `Priya@456` | Mild anemia detected. Iron-rich diet recommended. |
| `aman.verma@gmail.com` | `Aman@789` | Elevated cholesterol levels. Lifestyle changes advised. |
| `neha.desai@gmail.com` | `Neha@321` | Blood sugar within normal range. Continue healthy diet. |

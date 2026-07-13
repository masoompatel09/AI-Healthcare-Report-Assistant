# AI Healthcare Report Assistant 🏥

An AI-powered virtual healthcare assistant built with **Streamlit** and **Ollama (`gemma2:2b`)**. This application allows users to ask general healthcare questions and securely retrieve their personal medical report summaries, explained in patient-friendly, simple terms.

---

## 🌟 Key Features

- **🤖 General AI Healthcare Assistant**: Get instant responses to general health queries. The assistant is constrained by system prompts to prevent medical diagnosis or prescription.
- **🔒 Secure Patient Authentication**: Access reports via secure Email and Password matching from a mock patient database (`patients.xlsx`).
- **📋 Patient-Friendly AI Explanations**: Raw medical summaries are parsed and translated by the LLM into easy-to-understand language (under 150 words) with clear explanations of medical terminology.
- **🔗 Direct Download Link**: Upon successful authentication, users can request and retrieve a direct link to view their full reports.
- **🛡️ Security Session Lockout**: Prevents brute-forcing with a lockout mechanism that terminates the authentication process after 2 failed attempts.

---

## 📂 Project Structure

- [app.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/app.py) - Streamlit web application & user interface.
- [chat_engine.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/chat_engine.py) - Core dialog router and state machine ([SessionState](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/session.py)).
- [auth.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/auth.py) - User authentication logic using patient records loaded via [excel_loader.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/utils/excel_loader.py).
- [healthcare.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/healthcare.py) - Ollama wrapper for answering general health queries.
- [report_handler.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/report_handler.py) - Ollama wrapper for summarizing/explaining medical reports.
- [session.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/session.py) - Dataclass defining the state machine variables.
- [generate_patients.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/generate_patients.py) - Script to seed `patients.xlsx` with mock data.
- [utils/excel_loader.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/utils/excel_loader.py) - Helper functions using pandas to load patient data from Excel.
- `patients.xlsx` - Spreadsheet containing user credentials and report details.
- `.gitignore` - Git exclusion configurations.
- `test_*.py` - Standalone testing scripts for various modules (e.g., [test_auth.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/test_auth.py), [test_chat_engine.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/test_chat_engine.py), [test_healthcare.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/test_healthcare.py)).

---

## 🛠️ Prerequisites

Before running the application, make sure you have the following installed on your system:

1. **Python 3.8+**
2. **Ollama**:
   - Install Ollama from [ollama.com](https://ollama.com).
   - Pull the **Gemma 2 (2B)** model:
     ```bash
     ollama pull gemma2:2b
     ```
   - Ensure the Ollama service is running on your machine.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/masoompatel09/AI-Healthcare-Report-Assistant.git
cd AI-Healthcare-Report-Assistant
```

### 2. Create and Activate Virtual Environment
**On Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using `pip`:
```bash
pip install streamlit pandas openpyxl ollama
```

### 4. Seed the Database
Generate the initial database file `patients.xlsx` with sample accounts:
```bash
python generate_patients.py
```

### 5. Run the Application
Start the Streamlit development server:
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser to interact with the assistant.

---

## 🔑 Mock Accounts for Testing

The following credentials are generated in `patients.xlsx` for testing:

| Email ID | Password | Report Summary |
| :--- | :--- | :--- |
| `rahul.sharma@gmail.com` | `Rahul@123` | Blood pressure is normal. Mild Vitamin D deficiency detected. |
| `priya.patel@gmail.com` | `Priya@456` | Mild anemia detected. Iron-rich diet recommended. |
| `aman.verma@gmail.com` | `Aman@789` | Elevated cholesterol levels. Lifestyle changes advised. |
| `neha.desai@gmail.com` | `Neha@321` | Blood sugar within normal range. Continue healthy diet. |

*(For a full list of credentials, refer to [generate_patients.py](file:///c:/Users/jee14/OneDrive/Desktop/Project2_AI_Healthcare_Report_Assistant/generate_patients.py).)*

---

## 🔄 Conversational Flow

1. **General Chat**: The assistant functions in `NORMAL_CHAT` mode, fielding general healthcare questions.
2. **Intent Detection**: If a message requesting a report is detected (e.g., *"show my report"*), the application transitions state to `WAITING_EMAIL`.
3. **Authentication**:
   - The user is prompted for their email, then their password.
   - The inputs are verified against `patients.xlsx`.
   - On failure, users get a second attempt before the session is **LOCKED**.
4. **Explanation**: On success, the model explains the report summary in simple terms and asks if they want the full report link.
5. **Report Delivery**: Answering **Yes** outputs the direct download URL. Answering **No** returns the engine to general chat.

---

## 🧪 Testing the Components
You can test specific components of the assistant individually using the included standalone scripts:

- **Test Ollama connectivity:**
  ```bash
  python test_ollama.py
  ```
- **Test Authentication flow logic:**
  ```bash
  python test_auth.py
  ```
- **Test Report Explainer:**
  ```bash
  python test_report.py
  ```
- **Test Interactive Chat CLI:**
  ```bash
  python test_chat_engine.py
  ```

---

## ⚠️ Medical Disclaimer
This AI Healthcare Assistant is designed for informational purposes only. It does not provide medical diagnoses, prescribe treatment/medication, or replace professional clinical advice. Always consult a qualified medical professional for health concerns.

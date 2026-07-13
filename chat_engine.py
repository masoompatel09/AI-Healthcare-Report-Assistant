from healthcare import get_healthcare_response
from auth import authenticate_user
from session import SessionState
from report_handler import explain_report


class ChatEngine:

    def __init__(self):
        self.session = SessionState()

    def is_report_request(self, message: str) -> bool:
        """
        Detects whether the user is explicitly requesting
        access to THEIR OWN health report.
        """

        message = message.lower().strip()

        report_phrases = [
            "show my report",
            "show me my report",
            "view my report",
            "access my report",
            "retrieve my report",
            "download my report",
            "open my report",
            "i need my report",
            "give me my report",
            "my health report",
            "my medical report",
            "my blood report",
            "my lab report",
            "my mri report",
            "my ct scan report"
        ]

        return any(phrase in message for phrase in report_phrases)

    def process_message(self, message: str):

        # ==========================================
        # LOCKED
        # ==========================================

        if self.session.state == "LOCKED":
            return (
                "❌ Access denied.\n"
                "Maximum authentication attempts reached.\n"
                "Please start a new chat session."
            )

        # ==========================================
        # WAITING EMAIL
        # ==========================================

        if self.session.state == "WAITING_EMAIL":

            self.session.email = message.strip()
            self.session.state = "WAITING_PASSWORD"

            return "Please enter your password."

        # ==========================================
        # WAITING PASSWORD
        # ==========================================

        if self.session.state == "WAITING_PASSWORD":

            patient = authenticate_user(
                self.session.email,
                message.strip()
            )

            if patient:

                self.session.authenticated = True
                self.session.patient_data = patient
                self.session.state = "AUTHENTICATED"

                summary = patient["Report Summary"]

                ai_explanation = explain_report(summary)

                return (
                    "✅ **Authentication Successful!**\n\n"

                    "📋 **Original Report Summary**\n\n"
                    f"{summary}\n\n"

                    "🤖 **AI Explanation**\n\n"
                    f"{ai_explanation}\n\n"

                    "Would you like to receive your complete health report?\n"
                    "Reply with **Yes** or **No**."
                )

            self.session.attempts += 1

            if self.session.attempts >= 2:

                self.session.state = "LOCKED"

                return (
                    "❌ Invalid Email ID or Password.\n"
                    "Maximum authentication attempts reached.\n"
                    "Please start a new chat session."
                )

            self.session.state = "WAITING_EMAIL"

            return (
                "❌ Invalid Email ID or Password.\n\n"
                "Please enter your registered Email ID again."
            )

        # ==========================================
        # AUTHENTICATED
        # ==========================================

        if self.session.state == "AUTHENTICATED":

            response = message.strip().lower()

            if response in ["yes", "y"]:

                return (
                    "🔗 **Your Health Report**\n\n"
                    f"{self.session.patient_data['Report Link']}"
                )

            elif response in ["no", "n"]:

                self.session.state = "NORMAL_CHAT"
                self.session.authenticated = False
                self.session.patient_data = None
                self.session.email = ""
                self.session.attempts = 0

                return (
                    "You're welcome! 😊\n\n"
                    "If you have any healthcare-related questions, feel free to ask."
                )

            return "Please reply with **Yes** or **No**."

        # ==========================================
        # NORMAL CHAT
        # ==========================================

        if self.is_report_request(message):

            self.session.state = "WAITING_EMAIL"

            return (
                "Sure! I can help you access your health report.\n\n"
                "Please enter your registered Email ID."
            )

        # Everything else goes directly to Gemma

        return get_healthcare_response(message)
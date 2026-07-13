from dataclasses import dataclass


@dataclass
class SessionState:
    state: str = "NORMAL_CHAT"
    email: str = ""
    attempts: int = 0
    authenticated: bool = False
    patient_data: dict | None = None
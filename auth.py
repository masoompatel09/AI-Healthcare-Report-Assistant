from utils.excel_loader import load_patient_data


def authenticate_user(email: str, password: str):
    """
    Authenticate a user using email and password.

    Returns:
        dict | None
    """

    df = load_patient_data()

    if df.empty:
        print("Excel file could not be loaded.")
        return None

    # Remove extra spaces (if any)
    email = email.strip()
    password = password.strip()

    df["Email ID"] = df["Email ID"].astype(str).str.strip()
    df["Password"] = df["Password"].astype(str).str.strip()

    # Debug prints
    print("\n==============================")
    print("Entered Email   :", repr(email))
    print("Entered Password:", repr(password))

    print("\nExcel Data:")
    print(df[["Email ID", "Password"]])

    # Find matching user
    matched_user = df[
        (df["Email ID"] == email) &
        (df["Password"] == password)
    ]

    print("\nMatched User:")
    print(matched_user)
    print("==============================\n")

    if matched_user.empty:
        return None

    return matched_user.iloc[0].to_dict()
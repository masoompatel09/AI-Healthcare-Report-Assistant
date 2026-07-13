import pandas as pd


EXCEL_FILE = "patients.xlsx"


def load_patient_data():
    """
    Load patient data from the Excel file.

    Returns:
        pandas.DataFrame
    """
    try:
        df = pd.read_excel(EXCEL_FILE)
        return df

    except FileNotFoundError:
        print("Error: patients.xlsx not found.")
        return pd.DataFrame()

    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return pd.DataFrame()
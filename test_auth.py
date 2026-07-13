from auth import authenticate_user

email = "rahul.sharma@gmail.com"
password = "Rahul@13"

patient = authenticate_user(email, password)

if patient:
    print("Authentication Successful!\n")
    print(patient)
else:
    print("Invalid Email or Password.")
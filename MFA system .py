import pyotp

def generate_secret_key():
    return pyotp.random_base32()

def generate_and_verify_totp():
    secret_key = generate_secret_key()
    generated_code = pyotp.TOTP(secret_key).now()

    user_input = input(f"Generated TOTP Code for Login: {generated_code}\nEnter TOTP Code for Verification: ")

    if pyotp.TOTP(secret_key).verify(user_input):
        print("Verification Successful. Access Granted!")
    else:
        print("Verification Failed. Access Denied.")

if __name__ == "__main__":
    print("Two-Factor Authentication (TOTP) System")
    generate_and_verify_totp()

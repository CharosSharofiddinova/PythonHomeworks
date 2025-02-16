# Password Checker Task: Create a simple password checker.

#Ask the user to enter a password.
#If the password is shorter than 8 characters, print "Password is too short."
#If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.".
#If the password meets both criteria, print "Password is strong."

def check_password(password):
    """
    Checks if the password meets the required criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    """
    if len(password) < 8:
        print("❌ Password is too short.")
    elif not any(char.isupper() for char in password):
        print("❌ Password must contain an uppercase letter.")
    else:
        print("✅ Password is strong.")

# ✅ Get user input
password = input("🔑 Enter your password: ")
check_password(password)
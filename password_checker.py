import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength Result
    if strength == 5:
        result = "Strong Password ✅"
    elif strength >= 3:
        result = "Moderate Password ⚠️"
    else:
        result = "Weak Password ❌"

    return result, feedback


# Fixed Password
password = "Strong@123"

print("Password:", password)

result, feedback = check_password_strength(password)

print("\nPassword Strength:", result)

if feedback:
    print("\nSuggestions to improve your password:")
    for item in feedback:
        print("-", item)
else:
    print("Your password is secure.")

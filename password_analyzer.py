import string

password = input("Enter password: ")

score = 0

# Rule 1: Length
if len(password) >= 8:
    score += 1

# Rule 2: Uppercase
if any(c.isupper() for c in password):
    score += 1

# Rule 3: Lowercase
if any(c.islower() for c in password):
    score += 1

# Rule 4: Number
if any(c.isdigit() for c in password):
    score += 1

# Rule 5: Special character
if any(c in string.punctuation for c in password):
    score += 1

# Strength result
if score <= 2:
    print("❌ Password Strength: WEAK")
elif score == 3 or score == 4:
    print("⚠️ Password Strength: MEDIUM")
else:
    print("✅ Password Strength: STRONG")

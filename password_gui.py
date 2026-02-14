import tkinter as tk
import string

def check_password():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        result = "❌ WEAK\nEstimated crack time: Seconds"
    elif score == 3 or score == 4:
        result = "⚠️ MEDIUM\nEstimated crack time: Hours to days"
    else:
        result = "✅ STRONG\nEstimated crack time: Years"

    result_label.config(text=result)

def toggle_password():
    if show_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

# Window setup
window = tk.Tk()
window.title("Password Strength Analyzer")
window.geometry("850x250")

# Widgets
tk.Label(window, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(window, show="*", width=30)
entry.pack()

# Show password checkbox
show_var = tk.IntVar()
tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_var,
    command=toggle_password
).pack(pady=5)

tk.Button(window, text="Check Strength", command=check_password).pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 11))
result_label.pack(pady=10)

# Run app
window.mainloop()

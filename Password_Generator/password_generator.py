import tkinter as tk
import random
import string


# ---------- PASSWORD LOGIC ----------
def generate_password():
    try:
        length = int(length_var.get())

        if length < 4:
            result.set("Length too small (min 4)")
            return

        chars = string.ascii_letters + string.digits + string.punctuation

        password = "".join(random.choice(chars) for _ in range(length))

        result.set(password)

    except ValueError:
        result.set("Enter valid number")


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result.get())
    status.set("Copied to clipboard")


# ---------- GUI ----------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")


length_var = tk.StringVar()
result = tk.StringVar()
status = tk.StringVar()


tk.Label(root, text="Enter Password Length").pack(pady=5)
tk.Entry(root, textvariable=length_var).pack()


tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)


tk.Label(root, text="Generated Password:").pack()

tk.Entry(root, textvariable=result, width=40).pack(pady=5)


tk.Button(root, text="Copy Password", command=copy_password, bg="blue", fg="white").pack(pady=5)


tk.Label(root, textvariable=status, fg="darkblue").pack(pady=10)


root.mainloop()

import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user = comp = 0


def play(u):
    global user, comp
    c = random.choice(choices)

    if u == c:
        r.set(f"🤝 Draw! {c}")
    elif (u == "Rock" and c == "Scissors") or (u == "Paper" and c == "Rock") or (u == "Scissors" and c == "Paper"):
        user += 1
        r.set(f"🎉 Win! Computer: {c}")
    else:
        comp += 1
        r.set(f"😢 Lose! Computer: {c}")

    s.set(f"You: {user} | Computer: {comp}")


def reset():
    global user, comp
    user = comp = 0
    r.set("Game Reset 🔄")
    s.set("You: 0 | Computer: 0")


root = tk.Tk()
root.title("RPS 🎮")
root.geometry("360x250")
root.configure(bg="#1e1e2f")

r, s = tk.StringVar(), tk.StringVar()

tk.Label(root, text="Rock Paper Scissors", bg="#1e1e2f", fg="white",
         font=("Arial", 14, "bold")).pack(pady=8)

tk.Label(root, textvariable=r, bg="#1e1e2f", fg="yellow").pack()
tk.Label(root, textvariable=s, bg="#1e1e2f", fg="lightgreen").pack(pady=5)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=15)

tk.Button(frame, text="🪨", width=5, bg="green", fg="white",
          command=lambda: play("Rock")).grid(row=0, column=0, padx=3)

tk.Button(frame, text="📄", width=5, bg="blue", fg="white",
          command=lambda: play("Paper")).grid(row=0, column=1, padx=3)

tk.Button(frame, text="✂️", width=5, bg="orange", fg="white",
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=3)

tk.Button(root, text="Reset 🔄", bg="red", fg="white",
          command=reset).pack(pady=8)

root.mainloop()

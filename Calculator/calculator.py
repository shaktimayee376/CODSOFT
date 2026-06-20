import math
import customtkinter as ctk

# Theme and Appearance Setup
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"


class ModernCalculator(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window settings like a mobile screen layout
        self.title("Pro Calculator")
        self.geometry("360x520")
        self.resizable(False, False)

        self.expression = ""

        # --- Display Screen ---
        self.display = ctk.CTkEntry(
            self,
            placeholder_text="0",
            font=("Arial", 32, "bold"),
            justify="right",
            height=80,
            border_width=0,
            fg_color="transparent",
        )
        self.display.pack(fill="x", padx=20, pady=20)

        # --- Buttons Grid Layout ---
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # FIX: rowconfigure aur columnconfigure bina underscore (_) ke use hota hai
        for i in range(5):
            self.grid_frame.rowconfigure(i, weight=1, pad=8)
        for j in range(4):
            self.grid_frame.columnconfigure(j, weight=1, pad=8)

        self.create_buttons()

    def create_buttons(self):
        # Grid layout design (Mobile App Style)
        buttons = [
            ("C", 0, 0, "#E74C3C"),
            ("√", 0, 1, "#34495E"),
            ("^", 0, 2, "#34495E"),
            ("/", 0, 3, "#D35400"),
            ("7", 1, 0, None),
            ("8", 1, 1, None),
            ("9", 1, 2, None),
            ("*", 1, 3, "#D35400"),
            ("4", 2, 0, None),
            ("5", 2, 1, None),
            ("6", 2, 2, None),
            ("-", 2, 3, "#D35400"),
            ("1", 3, 0, None),
            ("2", 3, 1, None),
            ("3", 3, 2, None),
            ("+", 3, 3, "#D35400"),
            ("0", 4, 0, None),
            (".", 4, 1, None),
            ("sin", 4, 2, "#34495E"),
            ("=", 4, 3, "#2ECC71"),
        ]

        for text, row, col, color in buttons:
            fg_col = color if color else ("#2C3E50" if text.isdigit() else "#7F8C8D")

            btn = ctk.CTkButton(
                self.grid_frame,
                text=text,
                font=("Arial", 20, "bold"),
                fg_color=fg_col,
                height=60,
                corner_radius=12,  # Smooth rounded boxes like modern mobile UI
                command=lambda t=text: self.on_button_click(t),
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.update_display("0")
        elif char == "=":
            try:
                # Code safe evaluations for expressions like 2^3
                formatted_expr = self.expression.replace("^", "**")
                result = eval(formatted_expr)

                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                self.expression = str(result)
                self.update_display(self.expression)
            except ZeroDivisionError:
                self.update_display("Error: Div by 0")
                self.expression = ""
            except Exception:
                self.update_display("Error")
                self.expression = ""
        elif char == "√":
            try:
                val = float(self.display.get())
                res = math.sqrt(val)
                if res.is_integer():
                    res = int(res)
                self.expression = str(res)
                self.update_display(self.expression)
            except Exception:
                self.update_display("Error")
                self.expression = ""
        elif char == "sin":
            try:
                val = float(self.display.get())
                res = math.sin(math.radians(val))
                self.expression = str(round(res, 6))
                self.update_display(self.expression)
            except Exception:
                self.update_display("Error")
                self.expression = ""
        else:
            if self.expression == "0" or "Error" in self.expression:
                self.expression = ""
            self.expression += str(char)
            self.update_display(self.expression)

    def update_display(self, value):
        self.display.delete(0, ctk.END)
        self.display.insert(0, value)


if __name__ == "__main__":
    app = ModernCalculator()
    app.mainloop()
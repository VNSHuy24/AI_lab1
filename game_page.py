import tkinter as tk

class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Game in Progress...", font=("Helvetica", 25))
        label.pack(pady=50)

        end_button = tk.Button(self, text="End Game", font=("Helvetica", 25),
                               command=lambda: controller.show_frame("StartPage"))
        end_button.pack(pady=10)

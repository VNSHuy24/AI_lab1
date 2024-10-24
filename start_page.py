import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to the Game!", font=("Helvetica", 20, "bold"))
        label.pack(pady=50)

        start_button = tk.Button(self, text="Start Game", font=("Helvetica", 14),
                                 command=lambda: controller.show_frame("GamePage"))
        start_button.pack(pady=10)

        quit_button = tk.Button(self, text="Quit", font=("Helvetica", 14), command=controller.quit)
        quit_button.pack(pady=10)

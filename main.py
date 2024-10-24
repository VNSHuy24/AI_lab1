import tkinter as tk
from start_page import StartPage
from game_page import GamePage

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Game")
        self.geometry("400x300")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, GamePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()

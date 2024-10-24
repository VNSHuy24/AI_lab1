import tkinter as tk

# Lớp quản lý nhiều trang
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Game")
        self.geometry("400x300")

        # Container để chứa các trang
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Thêm các trang vào container
        for F in (StartPage, GamePage, EndPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Hiển thị trang bắt đầu
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()  # Đưa frame lên trên để hiển thị

# Trang bắt đầu
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

# Trang game chính
class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Game in Progress...", font=("Helvetica", 20))
        label.pack(pady=50)

        end_button = tk.Button(self, text="End Game", font=("Helvetica", 14),
                               command=lambda: controller.show_frame("EndPage"))
        end_button.pack(pady=10)

# Trang kết thúc
class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Game Over", font=("Helvetica", 20))
        label.pack(pady=50)

        restart_button = tk.Button(self, text="Restart Game", font=("Helvetica", 14),
                                   command=lambda: controller.show_frame("StartPage"))
        restart_button.pack(pady=10)

        quit_button = tk.Button(self, text="Quit", font=("Helvetica", 14), command=controller.quit)
        quit_button.pack(pady=10)

# Chạy ứng dụng
if __name__ == "__main__":
    app = GameApp()
    app.mainloop()

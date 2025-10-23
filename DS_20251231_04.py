import tkinter as tk

class MovingShapeApp:
    def __init__(self, root):
        self.root = root
        self.root = root.title("중간고사 4번")

        self.canvas = tk.Canvas(root, width = 400, height = 400, bg = "white")
        self.canvas.pack()

        
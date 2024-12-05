import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, *args):
        super().__init__()
        title, size, = args
        self.title(title)
        self.geometry(size)
        style = ttk.Style()
        style.theme_use("default")

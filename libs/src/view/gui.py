from tkinter import scrolledtext
from libs.src.utils.classes.App import App
from libs.src.controller.code_execution import execute_code
from tkinter import *
import tkinter as tk


class GuiTerminal(App):
    def __init__(self, *args):
        super().__init__(*args)
        self.configure(bg='#1a1b2f')
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self, bg='#1a1b2f')
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.code_input = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, bg='#2b2d4f', fg='#dcdcdc',
            insertbackground='#dcdcdc', font=('Courier', 12), borderwidth=0
        )
        self.code_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        button_frame = tk.Frame(frame, bg='#1a1b2f')
        button_frame.pack(pady=5)

        button = tk.Button(
            button_frame, text='Execute', command=self.read_code,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff', activeforeground='#1a1b2f',
            font=('Courier', 12), relief=FLAT, width=12
        )
        button.pack()

        self.result_output = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, state=tk.DISABLED, bg='#2b2d4f',
            fg='#dcdcdc', font=('Courier', 12), borderwidth=0
        )
        self.result_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=2)
        frame.rowconfigure(1, weight=0)
        frame.rowconfigure(2, weight=1)

    def read_code(self):
        input_code = self.code_input.get("1.0", tk.END).strip()
        result = execute_code(input_code)
        self.result_output.configure(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, result)
        self.result_output.configure(state=tk.DISABLED)

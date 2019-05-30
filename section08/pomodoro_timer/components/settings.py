import tkinter as tk
from tkinter import ttk

class Settings(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.settings_container = ttk.Frame(self, padding="30 15 30 15")
        self.settings_container.grid(row=0, column=0, sticky="EW")

        self.settings_container.columnconfigure(0, weight=1)
        self.settings_container.rowconfigure(1, weight=1)

        self.pomodoro_label = ttk.Label(self.settings_container, text="Pomodoro: ")
        self.pomodoro_label.grid(column=0, row=0, sticky="W")
        self.pomodoro_input = tk.Spinbox(
            self.settings_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.pomodoro,
            width=10,
        )
        self.pomodoro_input.grid(column=1, row=0, sticky="EW")
        self.pomodoro_input.focus()

        self.long_break_label = ttk.Label(self.settings_container, text="Long break time: ")
        self.long_break_label.grid(column=0, row=1, sticky="W")
        self.long_break_input = tk.Spinbox(
            self.settings_container,
            from_=0,
            to=60,
            increment=1,
            justify="center",
            textvariable=controller.long_break,
            width=10,
        )
        self.long_break_input.grid(column=1, row=1, sticky="EW")

        self.short_break_label = ttk.Label(self.settings_container, text="Short break time: ")
        self.short_break_label.grid(column=0, row=2, sticky="W")
        self.short_break_input = tk.Spinbox(
            self.settings_container,
            from_=0,
            to=30,
            increment=1,
            justify="center",
            textvariable=controller.short_break,
            width=10,
        )
        self.short_break_input.grid(column=1, row=2, sticky="EW")

        for child in self.settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)
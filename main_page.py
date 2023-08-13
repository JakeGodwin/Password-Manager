import customtkinter as ctk


class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self)
        self.label.configure(text="Hello World!")
        self.label.pack(fill="both", expand=True)

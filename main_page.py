import customtkinter as ctk

class MainPage(ctk.Frame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self)
        self.label.set_text("Hello World!")
        self.label.pack(fill=ctk.CTkLabel.FILL_BOTH, expand=True)
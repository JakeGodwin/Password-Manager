import customtkinter as ctk


class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        self.register_container = ctk.CTkFrame(self)
        self.register_container.pack(fill="both", expand=True)
        self.register_container.anchor(ctk.CENTER)

        self.register_page_frame = ctk.CTkFrame(self.register_container)
        self.register_page_frame.pack()

        self.register_label = ctk.CTkLabel(self.register_page_frame, text="Register Your account")
        self.register_label.pack()

        self.enter_register_username = ctk.CTkEntry(self.register_page_frame)
        self.enter_register_username.pack()

        self.enter_register_password = ctk.CTkEntry(self.register_page_frame)
        self.enter_register_password.pack()

        self.register_button_frame = ctk.CTkFrame(self.register_container)
        self.register_button_frame.pack()

        self.register_button = ctk.CTkButton(self.register_button_frame, text="Login")
        self.register_button.pack()

        self.go_back_button = ctk.CTkButton(self.register_button_frame, text="Back")
        self.go_back_button.pack()
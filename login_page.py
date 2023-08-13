import customtkinter as ctk
from main_page import MainPage


class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        self.login_container = ctk.CTkFrame(self)
        self.login_container.pack(fill="both", expand=True)
        self.login_container.anchor(ctk.CENTER)

        self.login_frame = ctk.CTkFrame(self.login_container)
        self.login_frame.pack()

        self.login_label = ctk.CTkLabel(self.login_frame, text="Login or Register")
        self.login_label.pack()

        self.enter_login_username = ctk.CTkEntry(self.login_frame)
        self.enter_login_username.pack()

        self.enter_login_password = ctk.CTkEntry(self.login_frame)
        self.enter_login_password.pack()

        self.login_button_frame = ctk.CTkFrame(self.login_container)
        self.login_button_frame.pack()

        self.login_button = ctk.CTkButton(
            self.login_button_frame,
            text="Login",
            command=lambda: self.controller.show_frame(MainPage),
        )
        self.login_button.pack()

        self.register_button = ctk.CTkButton(self.login_button_frame, text="Register")
        self.register_button.pack()

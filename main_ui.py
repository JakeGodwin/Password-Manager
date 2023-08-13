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
        self.login_frame.pack(padx=50, pady=50, expand=True)
        self.login_frame.anchor(ctk.CENTER)

        self.login_label = ctk.CTkLabel(
            self.login_frame, text="Login or Register", font=("Arial", 30)
        )
        self.login_label.pack(padx=50, pady=20, expand=True)

        self.enter_login_username = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="username",
            placeholder_text_color="grey",
            width=250,
            height=30,
        )
        self.enter_login_username.pack(padx=50, pady=10, expand=True)

        self.enter_login_password = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="password",
            placeholder_text_color="grey",
            width=250,
            height=30,
        )
        self.enter_login_password.pack(padx=50, pady=10, expand=True)

        self.login_button = ctk.CTkButton(
            self.login_frame,
            text="Login",
            command=lambda: self.controller.show_frame(MainPage),
        )
        self.login_button.pack(padx=50, pady=10, expand=True)

        self.register_button = ctk.CTkButton(
            self.login_frame,
            text="Register",
            command=lambda: self.controller.show_frame(RegisterPage),
        )
        self.register_button.pack(padx=50, pady=10, expand=True)

        self.login_text_label = ctk.CTkLabel(
            self.login_frame, text="Login or create an account!", font=("Arial", 18)
        )
        self.login_text_label.pack(padx=50, pady=10, expand=True)


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
        self.register_page_frame.pack(padx=50, pady=50, expand=True)
        self.register_page_frame.anchor(ctk.CENTER)

        self.register_label = ctk.CTkLabel(
            self.register_page_frame, text="Register Your account", font=("Arial", 30)
        )
        self.register_label.pack(padx=50, pady=50, expand=True)

        self.enter_register_username = ctk.CTkEntry(
            self.register_page_frame,
            placeholder_text="username",
            placeholder_text_color="grey",
            width=250,
            height=30,
        )
        self.enter_register_username.pack(padx=50, pady=10, expand=True)

        self.enter_register_password = ctk.CTkEntry(
            self.register_page_frame,
            placeholder_text="password",
            placeholder_text_color="grey",
            width=250,
            height=30,
        )
        self.enter_register_password.pack(padx=50, pady=10, expand=True)

        self.register_button = ctk.CTkButton(
            self.register_page_frame,
            text="Complete",
            command=lambda: self.controller.show_frame(MainPage),
        )
        self.register_button.pack(padx=50, pady=10, expand=True)

        self.go_back_button = ctk.CTkButton(
            self.register_page_frame,
            text="Back",
            command=lambda: self.controller.show_frame(LoginPage),
        )
        self.go_back_button.pack(padx=50, pady=10, expand=True)

        self.register_text_label = ctk.CTkLabel(
            self.register_page_frame, text="Create a new account!", font=("Arial", 18)
        )
        self.register_text_label.pack(padx=50, pady=10, expand=True)

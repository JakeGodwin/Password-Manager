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
        self.register_page_frame.pack(padx=50, pady=50, expand=True)
        self.register_page_frame.anchor(ctk.CENTER)

        self.register_label = ctk.CTkLabel(
            self.register_page_frame, text="Register Your account", font=("Arial", 30)
        )
        self.register_label.pack(padx=50, pady=50, expand=True)

        self.enter_register_username = ctk.CTkEntry(self.register_page_frame, placeholder_text="username", placeholder_text_color="grey", width=250, height=30)
        self.enter_register_username.pack(padx=50, pady=10, expand=True)

        self.enter_register_password = ctk.CTkEntry(self.register_page_frame, placeholder_text="password", placeholder_text_color="grey", width=250, height=30)
        self.enter_register_password.pack(padx=50, pady=10, expand=True)

        self.register_button = ctk.CTkButton(self.register_page_frame, text="Complete") #command=lambda: self.controller.show_frame(loginPage)
        self.register_button.pack(padx=50, pady=10, expand=True)

        self.go_back_button = ctk.CTkButton(self.register_page_frame, text="Back") # command=lambda: self.controller.show_frame(loginPage)
        self.go_back_button.pack(padx=50, pady=10, expand=True)

        self.register_text_label = ctk.CTkLabel(self.register_page_frame, text="Create a new account!", font=("Arial", 18))
        self.register_text_label.pack(padx=50, pady=10, expand=True)

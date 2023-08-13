import customtkinter as ctk
import main_page as MainPage
import main_application as MainApplication
import register_page as RegisterPage

class LoginPage(ctk.Frame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):  
        self.login_container = ctk.CTkFrame(self)
        self.login_container.pack(fill=ctk.BOTH, expand=True)
        self.login_container.anchor(ctk.CENTER)

        self.login_frame = ctk.CTkFrame(self.login_container)
        self.login_frame.pack()   #grid(row=0, column=0)
        
        self.login_label = ctk.CTkLabel(self.login_frame, text="Login or Register")
        self.login_label.pack() #grid(row=0, column=0)

        self.enter_login_username = ctk.CTkEntry(self.login_frame)
        self.enter_login_username.pack()  #grid(row=1, column=0)

        self.enter_login_password = ctk.CTkEntry(self.login_frame)
        self.enter_login_password.pack()  #grid(row=2, column=0)

        self.login_button_frame = ctk.CTkFrame(self.login_container)
        self.login_button_frame.pack() #grid(row=1, column=0)

        self.login_button = ctk.CTkButton(self.login_button_frame, text="Login", command=lambda: controller.show_frame(MainPage))
        self.login_button.pack()  #grid(row=0, column=0)

        self.register_button = ctk.CTkButton(self.login_button_frame, text="Register")
        self.register_button.pack()

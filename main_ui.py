import customtkinter as ctk
import tkinter as tk
import sqlite3
from user_database import UserDatabase as user_db
from accounts_database import AccountsDatabase as account_db
import bcrypt



class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        login_ref = LoginPage(parent, controller)
        self.accounts = []
        global login_id
        global logged_in_username
        logged_in_username = login_ref.get_logged_in_username()
        login_id = self.get_login_id(login_ref.get_logged_in_username())
        self.controller = controller
        if login_id is not None:
            self.load_user_accounts(login_id)
        self.main_page_container = ctk.CTkFrame(self)
        self.main_page_container.pack(fill="both", expand=True)
        self.main_page_container.anchor(ctk.CENTER)
        self.create_widgets()

    def create_widgets(self):
        self.left_side_frame = ctk.CTkFrame(self.main_page_container, fg_color="#2d2d2d")
        self.left_side_frame.pack(fill="both", expand=True, side="left") 
        self.left_side_frame.anchor(ctk.CENTER)    
        
        self.label_frame = ctk.CTkFrame(self.left_side_frame, fg_color="#2d2d2d")
        self.label_frame.grid(row=0, column=0)

        self.pass_label = ctk.CTkLabel(self.label_frame, text="View Passwords", bg_color="#2d2d2d")
        self.pass_label.grid(row=0, column=0, padx=20,pady=20)
        self.pass_label.anchor(ctk.CENTER)

        self.listbox_output_container = ctk.CTkFrame(self.left_side_frame, fg_color="#2d2d2d")
        self.listbox_output_container.grid(row=1, column=0)
        self.listbox_output_container.anchor(ctk.CENTER)

        self.list_box_frame = ctk.CTkFrame(self.listbox_output_container, fg_color="#2d2d2d")
        self.list_box_frame.grid(row=0, column=0)
        self.list_box_frame.anchor(ctk.CENTER)

        self.list_box = tk.Listbox(self.list_box_frame, width=30, height=20, bg="#32393d", borderwidth=0)
        self.list_box.grid(row=0, column=0, padx=20, pady=20)

        self.output_frame = ctk.CTkFrame(self.listbox_output_container, fg_color="#2d2d2d")
        self.output_frame.grid(row=0, column=1)

        self.output_box = ctk.CTkTextbox(self.output_frame,width=300, height=100, fg_color="#32393d")
        self.output_box.grid(row=0, column=0, padx=20, pady=20)

        self.coppy_button = ctk.CTkButton(self.output_frame, text="Copy Password")
        self.coppy_button.grid(row=1, column=0, padx=20, pady=20)

        self.left_side_button_frame = ctk.CTkFrame(self.left_side_frame, fg_color="#2d2d2d")
        self.left_side_button_frame.grid(row=2, column=0)

        self.edit_button = ctk.CTkButton(self.left_side_button_frame, text="edit")
        self.edit_button.grid(row=0, column=0, padx=20, pady=20)

        self.delete_button = ctk.CTkButton(self.left_side_button_frame, text="delete")
        self.delete_button.grid(row=0, column=1, padx=20, pady=20)

        self.right_side_frame = ctk.CTkFrame(self.main_page_container)
        self.right_side_frame.pack(fill="both", expand=True, side="right")
        self.right_side_frame.anchor(ctk.CENTER)

        self.right_side_label = ctk.CTkLabel(self.right_side_frame, text="Add New Password")
        self.right_side_label.grid(row=0, column=0, padx=20, pady=30)

        self.account_entry = ctk.CTkEntry(self.right_side_frame)
        self.account_entry.grid(row=1, column=0, padx=20, pady=10)

        self.password_entry = ctk.CTkEntry(self.right_side_frame)
        self.password_entry.grid(row=2, column=0, padx=20, pady=10)

        self.add_new_button = ctk.CTkButton(self.right_side_frame, text="Add", command=lambda: self.add_new_account(login_id, self.account_entry.get(), self.password_entry.get()))
        self.add_new_button.grid(row=3, column=0, padx=20, pady=20)

        self.sign_out_button = ctk.CTkButton(self.right_side_frame, text="Sign Out", command=lambda: self.controller.show_frame(LoginPage))
        self.sign_out_button.grid(row=4, column=0, padx=20, pady=40)

    def get_login_id(self, username):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            SELECT id FROM users WHERE username =?
        ''', (username,))
        user_id = self.cursor.fetchone()
        if user_id:
            return user_id[0]
        else:
            return None
        
    def add_new_account(self, user_id, account_name, password):
        self.conn = sqlite3.connect("accounts.db")
        self.cursor = self.conn.cursor()
        if account_name != "" and password!= "":
            self.cursor.execute('SELECT account_name FROM user_accounts WHERE user_id =?', [user_id])
            if self.cursor.fetchone() is not None:
                tk.messagebox.showerror("Error", "account already exists!, consider editing current account")
            else:
                account_db.insert_account(self, user_id, account_name, password)
                self.load_user_accounts()
                tk.messagebox.showinfo("account created", "Account created successfully!")
                
        else:
            tk.messagebox.showerror("Error", "Please fill in all fields!")

    def load_user_accounts(self):
        try:
            self.list_box.delete(0, tk.END)
            self.list_box.insert(tk.END, account_db.get_user_accounts(login_id))
        except:
            pass

    






    

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
            command=lambda: self.login_user()
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

    def login_user(self):
        login_username = self.enter_login_username.get()
        login_password = self.enter_login_password.get()
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        hashed_password = user_db.get_user_pass(self, login_username)
        if login_username != "" and login_password!= "":
            if hashed_password:
                if self.check_password(login_password, hashed_password):          
                    tk.messagebox.showinfo('Success', 'Login Successful!')
                    self.logged_in = True
                    self.get_logged_in_username()
                    self.controller.show_frame(MainPage)
            else:
                tk.messagebox.showinfo('Error', 'Invalid Username or Password!')
        else:
            tk.messagebox.showerror('Error', 'Please enter all fields!')

    def check_password(self, login_password, hashed_password):
        return bcrypt.checkpw(login_password.encode("utf-8"), hashed_password)
    
    def get_logged_in_username(self):
            logged_in_user = self.enter_login_username.get()
            return logged_in_user





class RegisterPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
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
        self.register_label.pack(padx=50, pady=20, expand=True)

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
            text="Sign Up",
            command=lambda: self.reg_new_user()
        )
        self.register_button.pack(padx=50, pady=10, expand=True)

        self.go_back_button = ctk.CTkButton(
            self.register_page_frame,
            text="Back",
            command=lambda: self.controller.show_frame(LoginPage)
        )
        self.go_back_button.pack(padx=50, pady=10, expand=True)

        self.register_text_label = ctk.CTkLabel(
            self.register_page_frame, text="Create a new account!", font=("Arial", 18)
        )
        self.register_text_label.pack(padx=50, pady=10, expand=True)

    def reg_new_user(self):
        username = self.enter_register_username.get()
        password = self.enter_register_password.get()
        password_hashed =bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        if username != "" and password!= "":
            self.cursor.execute('SELECT username FROM users WHERE username =?', [username])
            if self.cursor.fetchone() is not None:
                tk.messagebox.showerror("Error", "Username already exists!")
            else:
                user_db.add_user(self, username, password_hashed)
                tk.messagebox.showinfo("account created", "Account created successfully!")
                self.controller.show_frame(MainPage)
        else:
            tk.messagebox.showerror("Error", "Please fill in all fields!")

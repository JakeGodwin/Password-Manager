import customtkinter as ctk
from main_ui import MainPage, LoginPage, RegisterPage


class MainApplication(
    ctk.CTk
):  # main application class is the main application controller
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.geometry("1000x600")
        self.title("Password Manager")
        # container to hold different frames
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to store frames

        for F in (
            LoginPage,
            RegisterPage,
            MainPage,
        ):  # loops through page classes and creates frame objects
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)  # shows inital login page

    def show_frame(self, page_class):  # function to raise chosen frame to the top
        frame = self.frames[page_class]
        frame.tkraise()

    def run(self):  # function to run the application
    # if __name__ == "__main__":  # Entry point for running the application
        self.mainloop()
import customtkinter as CTk

class WarningWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Warning")
        self.label = CTk.CTkLabel(self, text="You must enter text")
        self.label.pack(padx=20, pady=20)
        self.button = CTk.CTkButton(self, text="Close", command=self.close_window)
        self.button.pack(padx=20, pady=20)

    def close_window(self):
        self.destroy()


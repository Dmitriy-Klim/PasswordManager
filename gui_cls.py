from tkinter import *
from tkinter import ttk

class MainWindow(Tk):



    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("625x330")
        self.resizable(False, False)

        self.passt = ""
        self.logint = ""
        self.sitet = ""

        login_label = ttk.Label(self, text="Username")
        login_label.config(font=("calibri", 10))
        login_label.grid(row=0, column=0, sticky="e", padx=10, pady=0)

        pass_label = ttk.Label(self, text="Password")
        pass_label.config(font=("calibri", 10))
        pass_label.grid(row=1, column=0, sticky="e", padx=10, pady=0)

        site_label= ttk.Label(self, text="The     site")
        site_label.config(font=("calibri", 10))
        site_label.grid(row=2, column=0, sticky="e", padx=10, pady=0)

        self.pass_field = ttk.Entry(self, show="*")
        self.pass_field.config(width=44)
        self.pass_field.insert(0, "")
        self.pass_field.grid(row=1, column=1, sticky="w", columnspan=2, padx=10, pady=0)

        self.login_field = ttk.Entry(self)
        self.login_field.config(width=64)
        self.login_field.insert(0, "")
        self.login_field.grid(row=0, column=1, columnspan=2, padx=10, pady=0)

        self.site_field = ttk.Entry(self)
        self.site_field.config(width=44)
        self.site_field.insert(0, "")
        self.site_field.grid(row=2, column=1, sticky="w", columnspan=2, padx=10, pady=0)

        self.tree = ttk.Treeview(self, columns=("Site", "Login", "Password"), show="headings")
        self.tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        self.tree.heading("Site", text="Site")
        self.tree.heading("Login", text="Login")
        self.tree.heading("Password", text="Password")








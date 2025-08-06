from sql import  *
from tkinter import *
from tkinter import ttk



class Update_Screen(Tk):

    def __init__(self, site, username, password):
        super().__init__()
        self.title ("Update Record")
        self.geometry ("400x100")
        self.resizable(width=False, height=False)
        self.old_site = site
        self.old_login = username
        self.old_password = password

        self.new_site = site
        self.new_login = username
        self.new_password = password

        username_label = Label(self, text="Username")
        username_label.grid(row=0, column=0, sticky="w", padx=10, pady=0)

        self.username_entry = Entry(self, width=45)
        self.username_entry.insert(0, username)
        self.username_entry.grid(row=0, column=1, sticky="e", padx=10, pady=0)

        password_label = Label(self, text="Password")
        password_label.grid(row=1, column=0, sticky="w", padx=10, pady=0)

        self.password_entry = Entry(self, width=45)
        self.password_entry.insert(0, password)
        self.password_entry.grid(row=1, column=1, sticky="e", padx=10, pady=0)

        site_label = Label(self, text="From what?")
        site_label.grid(row=2, column=0, sticky="w", padx=10, pady=0)

        self.site_entry = Entry(self, width=45)
        self.site_entry.insert(0, site)
        self.site_entry.grid(row=2, column=1, sticky="e", padx=10, pady=0)

        button_label = Label(self, text="Are you sure?")
        button_label.grid(row=3, column=0, sticky="w", padx=10, pady=0)

        confirm_button = Button(self, text="Yes - Confirm Changes", width=38, command=self.update_item)
        confirm_button.grid(row=3, column=1, sticky="e", padx=10, pady=0)

    def update_item(self):
        self.new_site = self.site_entry.get()
        self.new_login = self.username_entry.get()
        self.new_password = self.password_entry.get()
        update_item(self.new_site, self.new_login, self.new_password, self.old_site, self.old_login, self.old_password)

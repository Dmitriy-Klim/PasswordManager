import pyperclip
from gui_cls import *
from random import randint, sample, shuffle
import darkdetect
from update_scrn import *
from sql import *
from tkinter import messagebox

def setup_theme():
    style = ttk.Style()

    if darkdetect.theme() == "Dark":
        # Настройки для темной темы
        bg = "#2d2d2d"
        fg = "#ffffff"
        style.theme_use('alt')  # Альтернативная тема для темного режима

        # Конфигурация стилей
        style.configure('.', background=bg, foreground=fg)
        style.configure('TLabel', background=bg, foreground=fg)
        style.configure('TButton', background='#3d3d3d', foreground=fg)
        style.configure("Treeview",
                        font=('Arial', 10),
                        foreground="blue",  # Цвет шрифта
                        background="white",  # Цвет фона
                        fieldbackground="#9E9E9E")  # Цвет фона ячеек
        style.configure("TEntry",
                        font=('Arial', 10),
                        foreground="black",
                        background="white",
                        fieldbackground="#9E9E9E")

        style.map('TButton', background=[('active', '#4d4d4d')])
    else:
        # Настройки для светлой темы
        bg = "#f0f0f0"
        fg = "#000000"
        style.theme_use('clam')  # или 'vista', 'winnative'

        # Конфигурация стилей
        style.configure('.', background=bg, foreground=fg)

    return bg, fg

root = MainWindow()
bg, fg = setup_theme()
# Устанавливаем фон главного окна
root.configure(bg=bg)

def passwordgenerator():
    root.pass_field.delete(0, END)
    letters_in_password = randint(17,25)
    symbols_in_password = randint(5,8)
    numbers_in_passwords = randint(5,8)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    password_letters = sample(letters, letters_in_password - (symbols_in_password + numbers_in_passwords))
    password_symbols = sample(symbols, symbols_in_password)
    password_numbers = sample(numbers, numbers_in_passwords)
    password = password_letters + password_symbols + password_numbers
    shuffle(password)
    new_password = "".join(password)
    root.pass_field.insert(END, new_password)
    pyperclip.copy(new_password)

def add_new_item():
    login = root.login_field.get()
    password = root.pass_field.get()
    site = root.site_field.get()
    add_cred(site, login, password)
    root.login_field.delete(0, END)
    root.pass_field.delete(0, END)
    root.site_field.delete(0, END)
    root.tree.delete(*root.tree.get_children())
    get_all()

def get_all():
    root.tree.delete(*root.tree.get_children())
    result = get_all_from_db()
    for item in result:
        root.tree.insert("", END, values=item)

def remove_row():
    tree_focus = root.tree.focus()
    item_info = root.tree.item(tree_focus)
    item_text = item_info.get('values')
    remove_item(item_text[0], item_text[1], item_text[2])
    get_all()

def update_window():
    tree_focus = root.tree.focus()
    if tree_focus == "":
        pass
    else:

        item_info = root.tree.item(tree_focus)
        item_text = item_info.get('values')
        update = Update_Screen(item_text[0], item_text[1], item_text[2])
        update.mainloop()

def suarch_from_db():
    site = root.site_field.get()
    if site == "":
        pass
    else:
        result = search(site)
        if result == []:
            print("Site not found")
            messagebox.showinfo(title="Search Result", message="Site not found")
        else:
            messagebox.showinfo(title="Search Result", message=f" Site: {result[0][0]} \n Username: {result[0][1]} \n Password: {result[0][2]}")



run_button = ttk.Button(text="Add / New", command=add_new_item)
run_button.config(width=15)
run_button.grid(row=0, column=0, sticky="w", padx=10, pady=0)

rm_button = ttk.Button(text="Remove", command=remove_row)
rm_button.config(width=15)
rm_button.grid(row=1, column=0, sticky="w", padx=10, pady=0)

upd_button = ttk.Button(text="Update", command=update_window)
upd_button.config(width=15)
upd_button.grid(row=2, column=0, sticky="w", padx=10, pady=0)

gen_button = ttk.Button(text="Generate", command=passwordgenerator)
gen_button.config(width=15)
gen_button.grid(row=1, column=2, sticky="e", padx=10, pady=0)

search_button = ttk.Button(text="Search", command=suarch_from_db)
search_button.config(width=15)
search_button.grid(row=2, column=2, sticky="e", padx=10, pady=0)


get_all()
root.mainloop()

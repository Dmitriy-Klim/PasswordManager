import sqlite3


def add_cred(site, login, password):
    if site == "" and login == "" and password == "":
        pass
    else:
        con = sqlite3.connect('passwordManager.db', timeout=10)
        cur = con.cursor()
        cur.execute("INSERT INTO passmn (site, login, password) VALUES (?, ?, ?)",
                    (site, login, password))
        con.commit()
        con.close()

def get_all_from_db():
    con = sqlite3.connect('passwordManager.db', timeout=10)
    cur = con.cursor()
    cur.execute("SELECT * FROM passmn")
    rows = cur.fetchall()
    con.close()
    return rows

def remove_item(site, login, password):
    if site == "" and login == "" and password == "":
        pass
    else:
        con = sqlite3.connect('passwordManager.db', timeout=10)
        cur = con.cursor()
        cur.execute("DELETE FROM passmn WHERE site = ? AND login = ?", (site, login))
        con.commit()
        con.close()

def update_item(new_site, new_login, new_password, old_site, old_login, old_password):
    con = sqlite3.connect('passwordManager.db', timeout=10)
    cur = con.cursor()
    cur.execute("UPDATE passmn SET site = ?, login = ?, password = ? WHERE site = ? AND login = ?", (new_site, new_login, new_password, old_site, old_login))
    con.commit()
    cur.close()
    con.close()
    #print(f"{new_site} and {old_site} have been updated")

def search(site):
    con = sqlite3.connect('passwordManager.db', timeout=10)
    cur = con.cursor()
    cur.execute("SELECT * FROM passmn WHERE site = ?", (site,))
    rows = cur.fetchall()
    con.close()
    return rows
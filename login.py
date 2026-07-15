import tkinter as tk
from tkinter import messagebox
import subprocess

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "admin12345":
        messagebox.showinfo(
            "Login Berhasil",
            "Selamat datang di AntriKlinik Desktop"
        )

        root.destroy()
        subprocess.Popen(["python", "dashboard.py"])

    else:
        messagebox.showerror(
            "Login Gagal",
            "Username atau Password salah"
        )


root = tk.Tk()
root.title("Login AntriKlinik")
root.geometry("400x300")

judul = tk.Label(
    root,
    text="LOGIN ANTRIKLINIK",
    font=("Arial", 18, "bold")
)
judul.pack(pady=20)

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

btn_login = tk.Button(
    root,
    text="Login",
    command=login,
    width=15
)
btn_login.pack(pady=20)

root.mainloop()
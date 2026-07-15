import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox

try:
    with open("data_antrian.txt", "r") as file:
        jumlah = len(file.readlines())
        nomor_antrian = jumlah + 1
except FileNotFoundError:
    nomor_antrian = 1

data_antrian = []

koneksi = sqlite3.connect("../db.sqlite3")
cursor = koneksi.cursor()

cursor.execute("SELECT nama FROM blog_pasien")

data_pasien = cursor.fetchall()

daftar_pasien = []

for pasien in data_pasien:
    daftar_pasien.append(pasien[0])

koneksi.close()

def tambah_antrian():
    global nomor_antrian

    nama = combo_pasien.get()
    keluhan = entry_keluhan.get()

    if nama == "" or keluhan == "":
        messagebox.showwarning(
            "Peringatan",
            "Nama dan Keluhan harus diisi!"
        )
        return

    nomor = f"A{nomor_antrian:03d}"

    with open("data_antrian.txt", "a") as file:
        file.write(f"{nomor}|{nama}|{keluhan}\n")

    messagebox.showinfo(
        "Antrian Berhasil",
        f"Nomor Antrian : {nomor}\n"
        f"Nama Pasien : {nama}\n"
        f"Keluhan : {keluhan}"
    )

    data_antrian.append([
        nomor,
        nama,
        keluhan
    ])

    nomor_antrian += 1

    combo_pasien.set("")
    entry_keluhan.delete(0, tk.END)

root = tk.Tk()
root.title("Tambah Antrian")
root.geometry("450x350")

judul = tk.Label(
    root,
    text="FORM TAMBAH ANTRIAN",
    font=("Arial", 18, "bold")
)
judul.pack(pady=20)

tk.Label(root, text="Pilih Pasien").pack()

combo_pasien = ttk.Combobox(
    root,
    values=daftar_pasien,
    width=32
)

combo_pasien.pack(pady=5)

tk.Label(root, text="Keluhan").pack()
entry_keluhan = tk.Entry(root, width=35)
entry_keluhan.pack(pady=5)

btn_simpan = tk.Button(
    root,
    text="Simpan Antrian",
    command=tambah_antrian,
    width=20
)
btn_simpan.pack(pady=20)

root.mainloop()
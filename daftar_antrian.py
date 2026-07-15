import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Daftar Antrian")
root.geometry("700x400")

judul = tk.Label(
    root,
    text="DAFTAR ANTRIAN KLINIK",
    font=("Arial", 18, "bold")
)
judul.pack(pady=20)

table = ttk.Treeview(
    root,
    columns=("nomor", "nama", "keluhan"),
    show="headings"
)

table.heading("nomor", text="Nomor")
table.heading("nama", text="Nama Pasien")
table.heading("keluhan", text="Keluhan")

table.pack(fill="both", expand=True)

try:
    with open("data_antrian.txt", "r") as file:
        data = file.readlines()

    for item in data:
        nomor, nama, keluhan = item.strip().split("|")

        table.insert(
            "",
            tk.END,
            values=(nomor, nama, keluhan)
        )

except FileNotFoundError:
    pass

root.mainloop()
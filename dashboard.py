import tkinter as tk
import subprocess

def buka_antrian():
    subprocess.Popen(["python", "antrian.py"])

def buka_daftar():
    subprocess.Popen(["python", "daftar_antrian.py"])

def panggil_antrian():
    subprocess.Popen(["python", "panggil_antrian.py"])

root = tk.Tk()
root.title("Dashboard AntriKlinik")
root.geometry("700x500")

judul = tk.Label(
    root,
    text="DASHBOARD ANTRIKLINIK",
    font=("Arial", 22, "bold")
)
judul.pack(pady=30)
btn_tambah = tk.Button(
    root,
    text="Tambah Antrian",
    width=25,
    height=2,
    command=buka_antrian
    
)

btn_tambah.pack(pady=10)

btn_lihat = tk.Button(
    root,
    text="Lihat Daftar Antrian",
    width=25,
    height=2,
    command=buka_daftar
)
btn_lihat.pack(pady=10)

btn_panggil = tk.Button(
    root,
    text="Panggil Antrian Berikutnya",
    width=25,
    height=2,
    command=panggil_antrian
)
btn_panggil.pack(pady=10)

btn_keluar = tk.Button(
    root,
    text="Keluar",
    width=25,
    height=2,
    command=root.destroy
)
btn_keluar.pack(pady=10)

root.mainloop()
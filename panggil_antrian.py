import tkinter as tk
from gtts import gTTS
from playsound import playsound
import os

current = 0

def berikutnya():
    global current

    try:
        with open("data_antrian.txt", "r") as file:
            data = file.readlines()

        if current < len(data):
            nomor, nama, keluhan = data[current].strip().split("|")

            label_nomor.config(text=nomor)
            label_nama.config(text=nama)
            label_keluhan.config(text=keluhan)

            teks = f"Nomor antrian {nomor}, atas nama {nama}, silakan menuju ruang pemeriksaan."

            tts = gTTS(text=teks, lang="id")
            tts.save("suara.mp3")

            playsound("suara.mp3")

            os.remove("suara.mp3")

            current += 1

    except FileNotFoundError:
        label_nomor.config(text="Tidak ada data")


root = tk.Tk()
root.title("Panggil Antrian")
root.geometry("500x400")

judul = tk.Label(
    root,
    text="ANTRIAN YANG SEDANG DIPANGGIL",
    font=("Arial", 16, "bold")
)
judul.pack(pady=20)

label_nomor = tk.Label(
    root,
    text="-",
    font=("Arial", 35, "bold")
)
label_nomor.pack()

label_nama = tk.Label(
    root,
    text="-",
    font=("Arial", 20)
)
label_nama.pack(pady=10)

label_keluhan = tk.Label(
    root,
    text="-",
    font=("Arial", 16)
)
label_keluhan.pack(pady=10)

btn = tk.Button(
    root,
    text="Panggil Berikutnya",
    command=berikutnya,
    width=20,
    height=2
)
btn.pack(pady=20)

root.mainloop()
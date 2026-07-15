import sqlite3

koneksi = sqlite3.connect("../db.sqlite3")

cursor = koneksi.cursor()

cursor.execute("SELECT id, nama, umur, alamat, no_hp FROM blog_pasien")

data = cursor.fetchall()

for pasien in data:
    print(pasien)

koneksi.close()
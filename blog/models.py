from django.db import models

class Pasien(models.Model):
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    alamat = models.TextField()
    no_hp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class Dokter(models.Model):
    nama = models.CharField(max_length=100)
    spesialis = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class Obat(models.Model):
    nama_obat = models.CharField(max_length=100)
    stok = models.IntegerField()
    harga = models.IntegerField()

    def __str__(self):
        return self.nama_obat


class Pelayanan(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    dokter = models.ForeignKey(Dokter, on_delete=models.CASCADE)
    keluhan = models.TextField()
    diagnosa = models.TextField()
    tanggal = models.DateField()

    def __str__(self):
        return self.pasien.nama
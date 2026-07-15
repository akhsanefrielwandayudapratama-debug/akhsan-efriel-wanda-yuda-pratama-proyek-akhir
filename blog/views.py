from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Pasien, Dokter, Obat, Pelayanan
from django.http import HttpResponse
from reportlab.pdfgen import canvas


# ===================== HOME =====================

@login_required(login_url='login')
def home(request):

    cari = request.GET.get('cari')

    data_pasien = Pasien.objects.all()

    if cari:
        data_pasien = data_pasien.filter(
            Q(nama__icontains=cari) |
            Q(alamat__icontains=cari) |
            Q(no_hp__icontains=cari)
        )

    context = {
        'data_pasien': data_pasien,
        'jumlah_pasien': Pasien.objects.count(),
        'jumlah_dokter': Dokter.objects.count(),
        'jumlah_obat': Obat.objects.count(),
        'jumlah_pelayanan': Pelayanan.objects.count(),

        'grafik_label': ['Pasien', 'Dokter', 'Obat', 'Pelayanan'],
        'grafik_data': [
            Pasien.objects.count(),
            Dokter.objects.count(),
            Obat.objects.count(),
            Pelayanan.objects.count(),
        ],

        'cari': cari,
    }

    return render(request, 'home.html', context)


# ===================== PASIEN =====================

@login_required(login_url='login')
def tambah_pasien(request):

    if request.method == 'POST':

        Pasien.objects.create(
            nama=request.POST['nama'],
            umur=request.POST['umur'],
            alamat=request.POST['alamat'],
            no_hp=request.POST['no_hp']
        )

        messages.success(request, "Data pasien berhasil ditambahkan.")

        return redirect('home')

    return render(request, 'tambah_pasien.html')


@login_required(login_url='login')
def edit_pasien(request, id):

    pasien = Pasien.objects.get(id=id)

    if request.method == 'POST':

        pasien.nama = request.POST['nama']
        pasien.umur = request.POST['umur']
        pasien.alamat = request.POST['alamat']
        pasien.no_hp = request.POST['no_hp']

        pasien.save()

        messages.success(request, "✏️ Data pasien berhasil diperbarui.")

        return redirect('home')

    context = {
        'pasien': pasien
    }

    return render(request, 'edit_pasien.html', context)


@login_required(login_url='login')
def hapus_pasien(request, id):

    pasien = Pasien.objects.get(id=id)

    pasien.delete()

    messages.success(request, "🗑️ Data pasien berhasil dihapus.")

    return redirect('home')


# ===================== DOKTER =====================

@login_required(login_url='login')
def dokter(request):

    data_dokter = Dokter.objects.all()

    context = {
        'data_dokter': data_dokter
    }

    return render(request, 'dokter.html', context)


@login_required(login_url='login')
def tambah_dokter(request):

    if request.method == 'POST':

        Dokter.objects.create(
            nama=request.POST['nama'],
            spesialis=request.POST['spesialis'],
            no_hp=request.POST['no_hp']
        )

        messages.success(request, "👨‍⚕️ Data dokter berhasil ditambahkan.")

        return redirect('dokter')

    return render(request, 'tambah_dokter.html')


@login_required(login_url='login')
def edit_dokter(request, id):

    dokter = Dokter.objects.get(id=id)

    if request.method == 'POST':

        dokter.nama = request.POST['nama']
        dokter.spesialis = request.POST['spesialis']
        dokter.no_hp = request.POST['no_hp']

        dokter.save()

        messages.success(request, "✏️ Data dokter berhasil diperbarui.")

        return redirect('dokter')

    context = {
        'dokter': dokter
    }

    return render(request, 'edit_dokter.html', context)


@login_required(login_url='login')
def hapus_dokter(request, id):

    dokter = Dokter.objects.get(id=id)

    dokter.delete()

    messages.success(request, "🗑️ Data dokter berhasil dihapus.")

    return redirect('dokter')


# ===================== OBAT =====================

@login_required(login_url='login')
def obat(request):

    data_obat = Obat.objects.all()

    context = {
        'data_obat': data_obat
    }

    return render(request, 'obat.html', context)


@login_required(login_url='login')
def tambah_obat(request):

    if request.method == 'POST':

        Obat.objects.create(
            nama_obat=request.POST['nama_obat'],
            stok=request.POST['stok'],
            harga=request.POST['harga']
        )

        messages.success(request, "💊 Data obat berhasil ditambahkan.")

        return redirect('obat')

    return render(request, 'tambah_obat.html')


@login_required(login_url='login')
def edit_obat(request, id):

    obat = Obat.objects.get(id=id)

    if request.method == 'POST':

        obat.nama_obat = request.POST['nama_obat']
        obat.stok = request.POST['stok']
        obat.harga = request.POST['harga']

        obat.save()

        messages.success(request, "✏️ Data obat berhasil diperbarui.")

        return redirect('obat')

    context = {
        'obat': obat
    }

    return render(request, 'edit_obat.html', context)


@login_required(login_url='login')
def hapus_obat(request, id):

    obat = Obat.objects.get(id=id)

    obat.delete()

    messages.success(request, "🗑️ Data obat berhasil dihapus.")

    return redirect('obat')


# ===================== PELAYANAN =====================

@login_required(login_url='login')
def pelayanan(request):

    data_pelayanan = Pelayanan.objects.select_related('pasien', 'dokter')

    context = {
        'data_pelayanan': data_pelayanan
    }

    return render(request, 'pelayanan.html', context)


@login_required(login_url='login')
def tambah_pelayanan(request):

    if request.method == 'POST':

        Pelayanan.objects.create(
            pasien_id=request.POST['pasien'],
            dokter_id=request.POST['dokter'],
            keluhan=request.POST['keluhan'],
            diagnosa=request.POST['diagnosa'],
            tanggal=request.POST['tanggal']
        )

        messages.success(request, "🩺 Data pelayanan berhasil ditambahkan.")

        return redirect('pelayanan')

    context = {
        'pasien': Pasien.objects.all(),
        'dokter': Dokter.objects.all()
    }

    return render(request, 'tambah_pelayanan.html', context)


@login_required(login_url='login')
def edit_pelayanan(request, id):

    pelayanan = Pelayanan.objects.get(id=id)

    if request.method == 'POST':

        pelayanan.pasien_id = request.POST['pasien']
        pelayanan.dokter_id = request.POST['dokter']
        pelayanan.keluhan = request.POST['keluhan']
        pelayanan.diagnosa = request.POST['diagnosa']
        pelayanan.tanggal = request.POST['tanggal']

        pelayanan.save()

        messages.success(request, "✏️ Data pelayanan berhasil diperbarui.")

        return redirect('pelayanan')

    context = {
        'pelayanan': pelayanan,
        'pasien': Pasien.objects.all(),
        'dokter': Dokter.objects.all(),
    }

    return render(request, 'edit_pelayanan.html', context)


@login_required(login_url='login')
def hapus_pelayanan(request, id):

    pelayanan = Pelayanan.objects.get(id=id)

    pelayanan.delete()

    messages.success(request, "🗑️ Data pelayanan berhasil dihapus.")

    return redirect('pelayanan')


# ===================== LOGIN =====================

def login_admin(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Selamat datang di Sistem Informasi Klinik.")
            return redirect("home")

        messages.error(request, "Username atau password salah.")

    return render(request, "login.html")


def logout_admin(request):

    logout(request)

    messages.success(request, "Anda berhasil logout.")

    return redirect("login")

@login_required(login_url='login')
def laporan_pasien_pdf(request):

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="laporan_pasien.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(170, 800, "LAPORAN DATA PASIEN")

    p.setFont("Helvetica", 12)

    y = 760

    pasien = Pasien.objects.all()

    p.drawString(40, y, "No")
    p.drawString(80, y, "Nama")
    p.drawString(220, y, "Umur")
    p.drawString(280, y, "Alamat")
    p.drawString(430, y, "No HP")

    y -= 20

    nomor = 1

    for data in pasien:

        p.drawString(40, y, str(nomor))
        p.drawString(80, y, data.nama)
        p.drawString(220, y, str(data.umur))
        p.drawString(280, y, data.alamat)
        p.drawString(430, y, data.no_hp)

        nomor += 1
        y -= 20

    p.save()

    return response
from django.urls import path
from . import views

urlpatterns = [
    path(
    'laporan-pasien/',
    views.laporan_pasien_pdf,
    name='laporan_pasien_pdf'
),
    path('login/', views.login_admin, name='login'),
    path('logout/', views.logout_admin, name='logout'),
    path('', views.home, name='home'),
    path('tambah-pasien/', views.tambah_pasien, name='tambah_pasien'),
    path('edit-pasien/<int:id>/', views.edit_pasien, name='edit_pasien'),
    path('hapus-pasien/<int:id>/', views.hapus_pasien, name='hapus_pasien'),
    path('dokter/', views.dokter, name='dokter'),
    path('tambah-dokter/', views.tambah_dokter, name='tambah_dokter'),
    path('edit-dokter/<int:id>/', views.edit_dokter, name='edit_dokter'),
path('hapus-dokter/<int:id>/', views.hapus_dokter, name='hapus_dokter'),
path('obat/', views.obat, name='obat'),
path('tambah-obat/', views.tambah_obat, name='tambah_obat'),
path('edit-obat/<int:id>/', views.edit_obat, name='edit_obat'),
path('hapus-obat/<int:id>/', views.hapus_obat, name='hapus_obat'),
path('obat/', views.obat, name='obat'),
path('tambah-obat/', views.tambah_obat, name='tambah_obat'),
path('edit-obat/<int:id>/', views.edit_obat, name='edit_obat'),
path('hapus-obat/<int:id>/', views.hapus_obat, name='hapus_obat'),
path('pelayanan/', views.pelayanan, name='pelayanan'),
path('tambah-pelayanan/', views.tambah_pelayanan, name='tambah_pelayanan'),
path('edit-pelayanan/<int:id>/', views.edit_pelayanan, name='edit_pelayanan'),
path('hapus-pelayanan/<int:id>/', views.hapus_pelayanan, name='hapus_pelayanan'),
]
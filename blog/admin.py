from django.contrib import admin
from .models import Pasien, Dokter, Obat, Pelayanan

admin.site.register(Pasien)
admin.site.register(Dokter)
admin.site.register(Obat)
admin.site.register(Pelayanan)
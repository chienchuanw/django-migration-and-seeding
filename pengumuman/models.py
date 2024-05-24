from django.db import models
from django.utils import timezone


class Pengumuman(models.Model):
    deleted = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    tanggal_kelas = models.DateTimeField()
    pembuat = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    nama_mata_kuliah = models.ForeignKey("MataKuliah", on_delete=models.CASCADE)
    jenis_pengumuman = models.IntegerField()
    nama_dosen = models.CharField(max_length=255)
    nama_asisten = models.CharField(max_length=255)
    nama_ruang = models.ForeignKey("Ruang", on_delete=models.CASCADE)
    nama_sesi = models.ForeignKey("Sesi", on_delete=models.CASCADE)
    nama_status_pengumuman = models.ForeignKey(
        "StatusPengumuman", on_delete=models.CASCADE
    )
    komentar = models.TextField()

    def __str__(self):
        return f"{self.nama_dosen} - {self.jenis_pengumuman}"


class MataKuliah(models.Model):
    nama = models.CharField(max_length=255)


class Ruang(models.Model):
    nama = models.CharField(max_length=255)


class Sesi(models.Model):
    nama = models.CharField(max_length=255)


class StatusPengumuman(models.Model):
    nama = models.CharField(max_length=255)

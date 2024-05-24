from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)


class Meta:
    verbose_name = "admin"
    verbose_name_plural = verbose_name

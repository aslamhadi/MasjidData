from django.db import models


class Masjid(models.Model):
    name = models.CharField(max_length=255, default="")
    area = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    remarks = models.CharField(max_length=255, default="")

from django.db import models


class Masjid(models.Model):
    name = models.CharField(max_length=255, default="")
    area = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    remarks = models.CharField(max_length=255, default="")


class Hotel(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=50, default="")
    fax = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    website = models.CharField(max_length=200, default="")
    price = models.CharField(max_length=255, default="")
    other = models.CharField(max_length=255, default="")
    is_item_prayer = models.BooleanField(default=False)
    is_prayer_room = models.BooleanField(default=False)

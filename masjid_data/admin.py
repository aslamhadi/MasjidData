from django.contrib import admin

from masjid_data.models import Masjid


class MasjidAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'address', 'remarks')

admin.site.register(Masjid, MasjidAdmin)

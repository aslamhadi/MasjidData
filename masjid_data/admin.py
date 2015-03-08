import xlwt

from django.contrib import admin
from django.http import HttpResponse

from masjid_data.models import Masjid, Hotel


def download_excel_masjid(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=masjid.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Data")

    row_num = 0

    columns = [
        (u"Name", 2000),
        (u"Area", 6000),
        (u"Address", 8000),
        (u"Remarks", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    # queryset = Masjid.objects.all()
    for obj in queryset:
        row_num += 1
        row = [
            obj.name,
            obj.area,
            obj.address,
            obj.remarks,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def download_excel_hotel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=hotel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Data")

    row_num = 0

    columns = [
        (u"Country", 2000),
        (u"City", 2000),
        (u"Name", 4000),
        (u"Address", 8000),
        (u"Website", 4000),
        (u"Price", 6000),
        (u"Language", 8000),
        (u"Source", 8000),
        (u"Room", 2000),
        (u"Wifi", 2000),
        (u"Description", 10000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    # queryset = Masjid.objects.all()
    for obj in queryset:
        row_num += 1
        row = [
            obj.country,
            obj.city,
            obj.name,
            obj.address,
            obj.website,
            obj.price,
            obj.lang,
            obj.source,
            obj.room_count,
            obj.source,
            obj.other,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

download_excel_hotel.short_description = "Download as Excel"
download_excel_masjid.short_description = "Download as Excel"


class MasjidAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'address', 'remarks', 'source')
    actions = [download_excel_masjid]


class HotelAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'name', 'address', 'website', 'price', 'lang', 'source', 'room_count', 'wifi', 'other')
    actions = [download_excel_hotel]


admin.site.register(Masjid, MasjidAdmin)
admin.site.register(Hotel, HotelAdmin)

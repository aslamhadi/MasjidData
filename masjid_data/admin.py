import xlwt

from django.contrib import admin
from django.http import HttpResponse

from masjid_data.models import Masjid


def download_csv(modeladmin, request, queryset):
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

download_csv.short_description = "Download as Excel"


class MasjidAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'address', 'remarks')
    actions = [download_csv]

admin.site.register(Masjid, MasjidAdmin)

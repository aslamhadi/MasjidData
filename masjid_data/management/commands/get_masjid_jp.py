from django.core.management.base import BaseCommand

from masjid_data.models import Masjid
from masjid_data.utils import make_soup


def get_rows(section_url):
    soup = make_soup(section_url)
    div_center = soup.find("center")
    table = div_center.find("table")
    rows = table.findAll('tr')
    return rows

def get_columns(row):
    column = row.findAll("td")
    return column

class Command(BaseCommand):
    help = 'Scrap data from web'

    def handle(self, *args, **options):
        url = "http://masjid.jp/list.html"
        rows = get_rows(url)

        tds = []
        self.stdout.write('Now processing...')
        for row in rows:
            data = get_columns(row)
            masjid = Masjid()
            masjid.name = data[0].text
            masjid.area = data[1].text
            masjid.address = data[2].text
            masjid.source = url
            try:
                # font = data[3].findAll("font")
                # masjid.remarks = data[3].text
                masjid.remarks = data[3]
            except IndexError:
              pass

            masjid.save()
        self.stdout.write('Succesfully scrape the web')

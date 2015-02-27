from django.core.management.base import BaseCommand
from masjid_data.models import Masjid
from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://masjid.jp"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, 'lxml')

def get_rows(section_url):
    soup = make_soup(section_url)
    div_center = soup.find("center")
    table = div_center.find("table")
    rows = table.findAll('tr')
    # cols = rows.findAll('td')
    return rows

def get_columns(row):
    column = row.findAll("td")
    return column

class Command(BaseCommand):
    help = 'Scrap data from web'

    def handle(self, *args, **options):
        rows = get_rows("http://masjid.jp/list.html")

        tds = []
        for row in rows:
            data = get_columns(row)
            masjid = Masjid()
            masjid.name = data[0].text
            masjid.area = data[1].text
            masjid.address = data[2].text
            try:
                # font = data[3].findAll("font")
                # masjid.remarks = data[3].text
                masjid.remarks = data[3]
            except IndexError:
              pass

            masjid.save()
        self.stdout.write('Succesfully scrape the web')

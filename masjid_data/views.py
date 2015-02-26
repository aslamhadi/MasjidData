from bs4 import BeautifulSoup

from urllib2 import urlopen

from django.views import generic

from masjid_data.models import Masjid

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


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = 'masjid_list'

    def get_queryset(self):
      rows = get_rows("http://masjid.jp/list.html")

      return rows

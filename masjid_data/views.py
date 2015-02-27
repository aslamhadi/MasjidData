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

def get_columns(row):
    column = row.findAll("td")
    return column

def get_actual_data(td):
    data = td.find("font")
    return data

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = 'masjid_list'

    def get_queryset(self):
      # get row first
      rows = get_rows("http://masjid.jp/list.html")

      tds = []
      for row in rows:
          data = get_columns(row)
          masjid = {}
          masjid['name'] = data[0].text
          masjid['area'] = data[1].text
          masjid['address'] = data[2].text
          try:
              # font = data[3].findAll("font")
              # masjid.remarks = data[3].text
              masjid['remarks'] = data[3]
          except IndexError:
              pass
          tds.append(masjid)

      return tds

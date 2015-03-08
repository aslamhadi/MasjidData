from django.core.management.base import BaseCommand
from django.db import connection

from masjid_data.models import Hotel
from masjid_data.utils import make_soup

BASE_URL = "http://www.muslim-guide.jp"

def truncate_hotel():
    # for sqlite only
    cursor = connection.cursor()
    cursor.execute("DELETE FROM masjid_data_hotel")
    cursor.execute("VACUUM")

def get_url_detail(city):
    soup = make_soup(city['url'])

    hotel_list = soup.findAll('div', 'hotellist')
    hotel_urls = []
    for hotel in hotel_list:
        hotel_urls.append(BASE_URL + hotel.find("div", "hotellist_btn").a["href"])

    return hotel_urls, city['city']

def save_data(url, city):
    soup = make_soup(url)

    hotel_detail = soup.find("div", "table_def")
    table = hotel_detail.table
    rows = table.findAll("tr")

    hotel = Hotel()
    hotel.name = rows[0].td.text
    hotel.address = rows[1].td.text
    hotel.tel = rows[2].td.text
    hotel.room_count = rows[3].td.text
    hotel.price = rows[4].td.text
    hotel.wifi = rows[5].td.text
    hotel.lang = rows[6].td.text
    hotel.website = rows[7].td.text
    hotel.country = "Japan"
    hotel.city = city
    hotel.source = BASE_URL

    hotel_cc = soup.find("p", {"id": "hotel_cc"})
    hotel.other = hotel_cc.text

    hotel.save()

class Command(BaseCommand):
    help = 'Scrap data from web'

    def handle(self, *args, **options):
        self.stdout.write('Truncate data first...')
        truncate_hotel()

        tokyo = {"url":"http://www.muslim-guide.jp/hotel/area_tokyo.php", "city":"Tokyo"}
        kyoto = {"url":"http://www.muslim-guide.jp/hotel/area_kyoto.php", "city":"Kyoto"}
        osaka = {"url":"http://www.muslim-guide.jp/hotel/area_osaka.php", "city":"Osaka"}
        hokkaido = {"url":"http://www.muslim-guide.jp/hotel/area_hokkaido.php", "city":"Hokkaido"}
        cities = [tokyo, kyoto, osaka, hokkaido]

        self.stdout.write('Now processing...')
        for city in cities:
            hotel_urls, city_name = get_url_detail(city)
            self.stdout.write('Prosessing {}'.format(city_name))

            for url in hotel_urls:
                save_data(url, city_name)

        self.stdout.write('Succesfully scrape the web')

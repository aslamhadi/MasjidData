from bs4 import BeautifulSoup
from urllib2 import urlopen


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, 'lxml')

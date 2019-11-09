from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_usd_banki_ru(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html, "lxml")

    currency_table = BeautifulSoup(str(bsobj.findAll("", {"class": "currency-table__bordered-row"})[0]), "lxml")

    sale_place = currency_table.findAll("div", {"class": "currency-table__rate__text"})[1].get_text()

    buy_place = currency_table.findAll("div", {"class": "currency-table__rate__text"})[2].get_text()

    sale_price = currency_table.findAll("div", {"class": "currency-table__large-text"})[1].get_text().replace(',', '.')
    buy_price = currency_table.findAll("div", {"class": "currency-table__large-text"})[2].get_text().replace(',', '.')

    return {"sale_price": sale_price, "sale_place": sale_place, "buy_price": buy_price, "buy_place": buy_place}

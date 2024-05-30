import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open("hw33.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\r", delimiter=";")
        writer.writerow((data['name'], data['cost'], data['gpu'], data['cpu'], data['ram'], data['ssd']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    s1 = soup.find_all("div", class_="p-3 border border-secondary border-opacity-25")
    for soups in s1:
        name = soups.find("h3",
                          class_="woocommerce-loop-product__title text-center text-danger-emphasis fw-bold fs-4").text
        cost = soups.find("span", class_="fw-semibold text-white").text
        gpu = soups.find("ul", class_="d-flex flex-wrap mt-3 list-unstyled").find_all("div", class_="text-small")[
            1].text
        cpu = soups.find("ul", class_="d-flex flex-wrap mt-3 list-unstyled").find_all("div", class_="text-small")[
            3].text
        ram = soups.find("ul", class_="d-flex flex-wrap mt-3 list-unstyled").find_all("div", class_="text-small")[
            5].text
        ssd = soups.find("ul", class_="d-flex flex-wrap mt-3 list-unstyled").find_all("div", class_="text-small")[
            7].text

        data = {'name': name, 'cost': cost, 'gpu': gpu, 'cpu': cpu, 'ram': ram, 'ssd': ssd}
        write_csv(data)


def main():
    url = "https://delta-game.ru/kompyutery/?yclid=11506610639475048447"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

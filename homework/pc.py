import requests
from bs4 import BeautifulSoup


class Pc:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        pcs = self.html.find_all("div", class_="thumbnail")
        for pc in pcs:
            main = pc.find("h3", class_="topic-title").find("a").text
            href = pc.find("h3", class_="topic-title").find("a")["href"]
            title = pc.find("div", class_="topic-content text").text.strip()
            author = pc.find("a", class_="topic-info-author-link").text.strip()
            self.res.append({
                "title": title,
                "main": main,
                "author": author,
                "href": href
            })

    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                f.write(f"Название: {item['main']}\nКраткое описание:{item['title']}\nСсылка: {item['href']}\nАвтор: "
                        f"{item['author']}\n\n{'*' * 40}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

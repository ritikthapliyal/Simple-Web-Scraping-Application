from bs4 import BeautifulSoup
import requests
# import pprint

TARGET_URL = "https://www.nature.com/"

req = requests.get(TARGET_URL)
soup = BeautifulSoup(req.content, "html.parser")

region = soup.find("ul", class_="app-article-list-row")
content = region.find_all("li", class_="app-article-list-row__item")

news = []

for li in content:

    heading = li.find("h3").text
    summary = li.find("p").text
    img_url = li.find("img")["src"]

    data = {}
    data["heading"] = heading
    data["summary"] = summary
    data["img_url"] = img_url

    news.append(data)

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://www.washingtonpost.com/').text, "html.parser")
put = open("soup.prettify.txt", "w", encoding='utf-8')
put.write(soup.prettify())
put.close()
l_5 = [
        q.get_text()
        for q in soup.find_all(attrs=["headline small normal-style text-align-inherit ",
                                      "headline small thin-style text-align-inherit ",
                                      "headline xx-small normal-style text-align-inherit ",
                                      "headline x-small normal-style text-align-inherit ",
                                      "caption caption-small",
                                      "blurb normal normal-style ",
                                      "byline",
                                      "timestamp time"])
      ]
l_6 = [
        q.get_text()
        for q in soup.find_all("li", attrs={"class": "border-bottom-hairline-top-table"})
      ]
put = open("all_news.txt", "w", encoding='utf-8')
for i in l_5:
    put.write(i + '\n\n')
put.write("Блок 12 тем по 4 новости в каждой\n\n")
for i in l_6:
    put.write(i + '\n\n')
put.close()

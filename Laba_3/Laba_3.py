import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://www.washingtonpost.com/').text, "html.parser")
l_1 = [q.get_text() for q in soup.find_all("div", {"class": "headline small normal-style text-align-inherit "})]
l_2 = [q.get_text() for q in soup.find_all("div", {"class": "headline xx-small normal-style text-align-inherit "})]
l_3 = [q.get_text() for q in soup.find_all("div", {"class": "headline x-small normal-style text-align-inherit "})]
l_4 = [q.get_text() for q in soup.find_all("div", {"class": "headline small thin-style text-align-inherit "})]
l_5 = [q.get_text() for q in soup.find_all("li", {"class": "border-bottom-hairline-top-table"})]
put = open("headline.txt", "w", encoding='utf-8')
put.write('\n'.join(l_1)+'\n'+'\n'.join(l_2)+'\n'+'\n'.join(l_3)+'\n'+'\n'.join(l_4)+'\n'+'\n'.join(l_5))
put.close()
put = open("author.txt", "w", encoding='utf-8')
put.write('\n'.join({q.get_text() for q in soup.find_all("span", {"class": "author vcard"})}))
put.close()
put = open("annotation.txt", "w", encoding='utf-8')
put.write('\n\n'.join([q.get_text() for q in soup.find_all("div", {"class": "blurb normal normal-style "})]))
put.close()

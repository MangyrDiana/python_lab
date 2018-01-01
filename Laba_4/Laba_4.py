import requests
from bs4 import BeautifulSoup
from queue import Queue
import threading
import time


def get_posts(url, queue):
    posts = []
    while True:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        items = soup.find_all('div', [
            'moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false full pb-feature pb-layout-item pb-f-homepage-story',
            'moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false col-md-6 pb-feature pb-layout-item pb-f-homepage-story col-sm-6 col-xs-12 col-lg-6',
            'moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false col-xs-4 pb-feature pb-layout-item pb-f-homepage-story',
            'moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false pb-feature pb-layout-item pb-f-homepage-card col-lg-3 col-sm-6 col-xs-12 col-md-4'])
        for item in items:
            try:
                label = item.find('div', [' label label-normal label-small label-primary',
                                          ' label label-normal label-primary']).text
            except AttributeError:
                label = 'label = N/A'
            try:
                datetime = item.find('li', {'class': 'timestamp time'}).text
            except AttributeError:
                datetime = 'datetime = N/A'
            try:
                byline = item.find('li', {'class': 'byline'}).text
            except AttributeError:
                byline = 'author = N/A'
            try:
                content = item.find('div', {'data-pb-field': 'summary'}).text
            except AttributeError:
                content = 'content = N/A'
            titles = item.find_all('a', {'data-pb-field': 'web_headline'})
            for i in titles:
                title = i.text
                if title not in posts:
                    posts.append(title)
                    queue.put({
                        'datetime': datetime,
                        'author': byline,
                        'title': title,
                        'content': content,
                        'label': label})
        time.sleep(10)


queue = Queue()
url = 'https://www.washingtonpost.com'
thread = threading.Thread(target=get_posts, args=(url, queue))
thread.start()
while True:
    news = queue.get()
    if news['label'] != 'label = N/A':
        print(news['label'])
    if news['datetime'] != 'datetime = N/A':
        print(news['datetime'])
    print(news['title'])
    print(news['content'])
    print(news['author'])
    print('\n')
    time.sleep(1)


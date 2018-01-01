import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://www.washingtonpost.com').text, "html.parser")
posts = []
items = soup.find_all('div', ['moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false full pb-feature pb-layout-item pb-f-homepage-story',
                              'moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false col-md-6 pb-feature pb-layout-item pb-f-homepage-story col-sm-6 col-xs-12 col-lg-6',
                              'moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false col-xs-4 pb-feature pb-layout-item pb-f-homepage-story',
                              'moat-trackable pb-f-theme-normal pb-f-dehydrate-false pb-f-async-false pb-feature pb-layout-item pb-f-homepage-card col-lg-3 col-sm-6 col-xs-12 col-md-4'])
for item in items:
    try:
        label = item.find('div', [' label label-normal label-small label-primary', ' label label-normal label-primary']).text
    except AttributeError:
        label = 'label = N/A'
    try:
        datetime = item.find('li', {'class':'timestamp time'}).text
    except AttributeError:
        datetime = 'datetime = N/A'
    try:
        byline = item.find('li', {'class':'byline'}).text
    except AttributeError:
        byline = 'author = N/A'
    try:
        content = item.find('div', {'data-pb-field':'summary'}).text
    except AttributeError:
        content = 'content = N/A'
    titles = item.find_all('a', {'data-pb-field':'web_headline'})
    for i in titles:
        title = i.text
        posts.append({
            'datetime':datetime,
            'author':byline,
            'title':title,
            'content':content,
            'label':label})

for i in range(len(posts)):
    if posts[i]['label'] != 'label = N/A':
        print(posts[i]['label'])
    if posts[i]['datetime'] != 'datetime = N/A':
        print(posts[i]['datetime'])
    print(posts[i]['title'])
    print(posts[i]['content'])
    print(posts[i]['author'])
    print('\n')



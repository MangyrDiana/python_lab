import re
import requests


def get_adr(new_adr, seen, ttt):
    words = [
             q
             for i in range(len(new_adr))
             for text in requests.get(new_adr[i]).text.split(' ')
             for q in re.findall('href="/.+/"', text)
            ]
    words = {
             'http:/' + words[i][7:len(words[i]) - 2] + '/'
             if words[i][7] == '/'
             else 'http://www.mosigra.ru/' + words[i][7:len(words[i]) - 2] + '/'
             for i in range(len(words))
            }
    new_adr = [x for x in words if x not in seen]
    for x in words:
        if x not in seen:
            seen.append(x)
    if len(new_adr) > 2:
        get_adr(new_adr, seen, ttt)
    else:
        put = open("all_адреса_сайта_тест.txt", "w", encoding='utf-8')
        put.write('\n'.join(seen))
        put.close()
        return seen


def adr_mail(c):
    words = {
             q
             for gr_1 in range(len(c))
             for text in requests.get(c[gr_1]).text.split(' ')
             for q in re.findall('[\w.][\w.]+@\w+\.\w+', text)
            }
    viv = open("сортированные_почты.txt", "w", encoding='utf-8')
    viv.write('\n'.join(words))
    viv.close()

adr_mail(get_adr(new_adr=['http://www.mosigra.ru/'], seen=['http://www.mosigra.ru/'], ttt=0))

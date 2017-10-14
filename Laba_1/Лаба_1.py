import re
import requests

words = []
seen = []
text = requests.get('http://www.mosigra.ru/').text.split(' ')
for word in text:
    m = re.findall('\w+@\w+\.\w+', word)
    if m:
        words += m
for x in words:
    if x not in seen:
        seen.append(x)
my_input = open("Адреса_Лаба_1.txt", "w", encoding='utf-8')
my_input.write('\n'.join(seen))
my_input.close()





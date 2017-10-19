import re
import requests

print({q for word in requests.get('http://www.mosigra.ru/').text.split(' ') for q in re.findall('\w+@\w+\.\w+', word)})

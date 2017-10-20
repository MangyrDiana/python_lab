import re
import requests

print({q for q in re.findall('\w+@\w+\.\w+', requests.get('http://www.mosigra.ru/').text)})

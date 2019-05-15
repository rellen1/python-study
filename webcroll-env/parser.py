import requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/beomi.github.io_old/')

html = req.text
# header = req.headers
# status = req.status_code
# is_ok = req.ok
soup = BeautifulSoup(html, 'html.parser')

print(soup)
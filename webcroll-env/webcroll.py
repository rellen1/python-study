import urllib.request
from bs4 import BeautifulSoup

url = "http://naver.com"
req = urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode, "html.parser")

print(soup)
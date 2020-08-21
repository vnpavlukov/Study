import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url_1 = 'http://py4e-data.dr-chuck.net/comments_42.html'
url_2 = 'http://py4e-data.dr-chuck.net/comments_810456.html'

urls = [url_1, url_2]

for url in urls:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('td')

    for tag in tags:
        print(tag.get('class'))

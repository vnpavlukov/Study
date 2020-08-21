import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def return_url_by_count(inp_url, imp_num):
    html = urllib.request.urlopen(inp_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = 0
    tags = soup('a')
    for tag in tags:
        count += 1
        if count == imp_num:
            return tag.get('href', None)


def find_the_lust_url(first_url, position, repeats):
    print(first_url)
    new_url = return_url_by_count(first_url, position)
    print(new_url)
    while repeats:
        new_url = return_url_by_count(new_url, position)
        repeats -= 1
        print(new_url)
    return return_url_by_count(new_url, position)


url_1 = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url_2 = 'http://py4e-data.dr-chuck.net/known_by_Carron.html'

lust_url = find_the_lust_url(url_1, 3, 2)
lust_name = re.search(r'by_(.*)\.', lust_url)
print(lust_name.group(1))

lust_url = find_the_lust_url(url_2, 18, 7)
lust_name = re.search(r'by_(.*)\.', lust_url)
print(lust_name.group(1))

import urllib.request
import xml.etree.ElementTree as ET


url_1 = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url_2 = 'http://py4e-data.dr-chuck.net/comments_810458.xml'
urls = [url_1, url_2]

for url in urls:
    data = urllib.request.urlopen(url).read()
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    sum_of_numb = 0
    for item in lst:
        sum_of_numb += int(item.find('count').text)
    print(sum_of_numb)

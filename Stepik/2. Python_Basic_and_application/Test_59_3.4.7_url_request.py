import requests
import re

input_url = 'http://pastebin.com/raw/hfMThaGb'
# input_url = input()
# data = requests.get(input_url).text
# print(data)

pattern = r"<a?.+href=['\" ]?(.+?://)?(w?w?w?\.?\w+-?\w+?\.\w+-?[\.]?\w+[\.]?(\w+)?)"


def find_all_links(data):
    tuple_links = re.findall(pattern, requests.get(data).text)
    return set(tuple_links)


set_links = set()

for link in find_all_links(input_url):
    # print(link)
    set_links.add(link[1])

for i in sorted(set_links):
    print(i)
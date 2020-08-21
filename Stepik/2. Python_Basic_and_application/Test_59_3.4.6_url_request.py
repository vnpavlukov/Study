import requests
import re

input_url = 'http://pastebin.com/raw/7543p0ns'


# first_req = input()


def find_all_links(link):
    tuple_links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]',
                             requests.get(link).text)
    return set(tuple_links)


for i in sorted(find_all_links(input_url)):
    print(i)

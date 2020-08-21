import requests
import re

# first_req = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
# second_req = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'


first_req = input()
second_req = input()


def tuple_links_in_first_link(link, check_link):
    tuple_links = re.findall(r'https://.+?html',
                             requests.get(link).text)
    for link in tuple_links:
        new_tuple_links = re.findall(r'https://.+?html',
                                    requests.get(link).text)
        if check_link in new_tuple_links:
            return "Yes"

    return "No"


print(tuple_links_in_first_link(first_req, second_req))
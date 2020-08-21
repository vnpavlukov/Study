import requests

get_url = requests.get(
    'https://stepic.org/media/attachments/course67/3.6.2/699.txt')

imp_text = get_url.text

count = 0
for i in imp_text.splitlines():
    count += 1

print(count)

import requests

first = '213837.txt'
get_url = requests.get(
    'https://stepic.org/media/attachments/course67/3.6.3/' + first)

imp_text = get_url.text

print(imp_text)

while imp_text[0:1] != 'We':
    get_url = requests.get(
        'https://stepic.org/media/attachments/course67/3.6.3/' + first)
    imp_text = get_url.text
    first = imp_text
    print(first)

print(imp_text)

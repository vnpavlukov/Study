import requests

response = requests.get('https://ya.ru/white')

code = response.status_code
print(f'Код ответа = {code}')

headers = response.headers
print(f'Тип содержимого: {headers["content-type"]}')
print(f'Время ответа: {headers["date"]}')

print('---')
for i, h in headers.items():
    print(i, ':\t\t\t\t', h)
    print()

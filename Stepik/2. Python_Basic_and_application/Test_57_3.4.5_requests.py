import requests

res = requests.get('https://docs.python.org/3.5/')
print(res.status_code)  # запрос на существование страницы
print(res.headers('Content-Type'))
# print(res.content)  # данные самой страницы в бинарном виде
# print(res.text)  # данные самой страницы в текстовом виде

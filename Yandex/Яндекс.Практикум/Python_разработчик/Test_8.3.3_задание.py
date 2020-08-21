import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'
}

response = requests.get(url, headers=request_headers, params=weather_parameters)
print(response.text)

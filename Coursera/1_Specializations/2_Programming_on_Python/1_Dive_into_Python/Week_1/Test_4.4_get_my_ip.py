import requests


def get_location_info():
    return requests.get('https://freegeoip.app/json/').json()


if __name__ == "__main__":
    info = get_location_info()
    for key, value in info.items():
        print(key, value, sep='\t')

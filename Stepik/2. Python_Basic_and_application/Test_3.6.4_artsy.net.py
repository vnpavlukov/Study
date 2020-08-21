import requests
import json


def get_token():
    client_id = '88c9dc22861f560f8110'
    client_secret = 'f92b7a4e77134c86ed4c0a2eff3d891e'

    req = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                        data={
                            "client_id": client_id,
                            "client_secret": client_secret
                        })
    data = json.loads(req.text)
    return data["token"]


def get_author_attribute(a_id, token):
    r = requests.get("https://api.artsy.net/api/artists/" + a_id,
                     headers={"X-Xapp-Token": token})
    author = json.loads(r.text)
    return {author['sortable_name']: author['birthday']}


my_token = get_token()

dict_artist = {}
with open('Test_3.6.4_artsy.net.data.txt') as file:
    for line in file:
        new_id = line.rstrip()
        dict_artist.update(get_author_attribute(new_id, my_token))

sorted_dict = sorted(dict_artist.items(), key=lambda x: (x[1], x[0]))

for year_name in sorted_dict:
    print(year_name[0])

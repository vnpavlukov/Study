import json

input_json_data =  json.loads(input())
# input_json_data = '[' \
#                   '{"name": "beta", "parents": ["alpha", "gamma"]},' \
#                   '{"name": "gamma", "parents": ["alpha"]},' \
#                   '{"name": "alpha", "parents": []},' \
#                   '{"name": "delta", "parents":["gamma", "zeta"]},' \
#                   '{"name": "epsilon", "parents":["delta"]},' \
#                   '{"name": "zeta", "parents":[]}' \
#                   ']'

for i in input_json_data:
    print(i)
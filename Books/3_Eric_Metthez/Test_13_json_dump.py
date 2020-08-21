import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'Test_13_json.json'
with open(filename, 'w') as file:
    json.dump(numbers, file)

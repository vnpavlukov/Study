import json

filename = 'Test_13_json.json'
with open(filename) as file:
    numbers = json.load(file)

print(numbers)

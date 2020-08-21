import requests
import re

numbers = []
with open('Test_60_3.6.3_boring_request.txt', 'r') as f:
    for line in f:
        numbers.append(line.rstrip())

for number in numbers:
  input_url = 'http://numbersapi.com/' + str(number) + '/math?json=true'
  tuple_links = re.findall(r'\"found\":.(.*?),', requests.get(input_url).text)
  print('Interesting') if tuple_links[0] == 'true' else print('Boring')

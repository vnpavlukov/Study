import re

result = re.findall(r'[89]\d{9}',
                    '9999999999, 999999-999, 99999x9999')

line = 'asdf fjdk;afed,fjek,asdf,foo'
#result = re.split(r'[;,\s]', line)
#print(result)

line = '1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5Will' \
       'iamAva6EthanMia7MichaelEmily'

result = re.findall(r'\d([\w])]', line)
print(result)
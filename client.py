import requests


requests.put('http://localhost:8489/stack/arguments', json={'arguments': ['3', '0', '5'],
                                                                           'operation': 'divide'})

x = requests.get('http://localhost:8489/stack/size')

print(x.text)

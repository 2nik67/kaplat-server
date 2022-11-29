import requests


requests.put('http://localhost:8489/stack/arguments', json={'arguments': [3, 0, 5],
                                                                           'operation': 'divide'})

x = requests.get('http://localhost:8489/stack/size')
delete = requests.delete('http://localhost:8489/stack/arguments', params={'count': '5'})


print(delete.text)


calc = requests.get('http://localhost:8489/stack/operate', params={'operation': 'fact'})
print(calc.text)
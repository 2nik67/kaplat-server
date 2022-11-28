import requests


x = requests.post('http://localhost:8489/independent/calculate', json={'arguments': ['3', '0'],
                                                                           'operation': 'divide'})

print(x.text)

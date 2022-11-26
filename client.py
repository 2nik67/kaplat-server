import requests

if __name__ == '__main__':
    x = requests.post('http://localhost:8489/independent/calculate', json={'arguments': ['3', '4'],
                                                                           'operation': 'plus'})

    print(x.text)

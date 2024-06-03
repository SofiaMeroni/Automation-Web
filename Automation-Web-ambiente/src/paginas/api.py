import requests

def todaslasbromas(num_bromas):
    bromas = []
    for _ in range(num_bromas):
        response = requests.get('https://api.chucknorris.io/jokes/random')
        if response.status_code != 200:
            print("La prueba falló")
            break
        data = response.json()
        broma = data['value']
        bromas.append(broma)
    return bromas



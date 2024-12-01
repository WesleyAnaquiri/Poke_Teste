import requests

def test_listar_habilidades():
    url = "https://pokeapi.co/api/v2/ability/?limit=5"
    resposta = requests.get(url)
    assert resposta.status_code == 200  
    dados = resposta.json()

    print("Habilidades encontradas:")
    for habilidade in dados['results']:
        print(f" - {habilidade['name']}")

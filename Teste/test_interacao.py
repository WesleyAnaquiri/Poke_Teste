import requests

def test_buscar_pokemon_interativo():
    nome_pokemon = input("Digite o nome do Pokémon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"Nome: {dados['name']}")
        print(f"Altura: {dados['height']} dm")
        print(f"Peso: {dados['weight']} hg")
        print(f"Tipos: {[tipo['type']['name'] for tipo in dados['types']]}")
        assert True  
    else:
        print("Poxa! Não encontramos seu Pokemon!")
        assert resposta.status_code == 404  

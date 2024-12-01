import requests

def test_pokemon_inexistente():
    nome_pokemon = "PokeErro"
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    resposta = requests.get(url)

    print("Teste de erro: Este Pokémon Não Existe!.")
    print(f"Status retornado: {resposta.status_code}")
    
    assert resposta.status_code == 404  
    

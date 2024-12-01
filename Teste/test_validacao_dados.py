import requests

def test_validar_dados_pokemon():
    nome_pokemon = "charizard"
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    resposta = requests.get(url)
    assert resposta.status_code == 200 
    dados = resposta.json()

    print(f"Nome: {dados['name']}")
    print(f"ID: {dados['id']}")
    print(f"Base de Experiência: {dados['base_experience']}")

  # Você pode trocar o nome do Pokemon caso queira ver essas informações sobre outro.
    assert dados["name"] == "charizard"
    assert isinstance(dados["base_experience"], int)
    assert dados["base_experience"] > 0


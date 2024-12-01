Este repositório contém testes de integração com a PokeAPI.

API USADA: *PokéAPI*

SOBRE A API:  uma API pública que fornece dados sobre os Pokémon, incluindo informações como nome, altura, peso, habilidades e muito mais.
Retorna detalhes sobre uma habilidade específica de um Pokémon.
Fornece informações sobre a espécie de um Pokémon.

Dependencias:
*Python 3 ou superior*
*Biblioteca requests*: Para fazer as requisições HTTP à API.
*pytest*: Para rodar os testes.

Sobre os Testes:
*test_erro_pokemon.py*: Testa cenários em que o Pokémon solicitado não existe.
*test_interacao.py*: Testa a interação com o usuário, onde o nome do Pokémon é fornecido e as informações são exibidas.
*test_sucesso_habilidade.py*: Testa a obtenção de habilidades dos Pokémons.
*test_sucesso_pokemon.py*: Testa a obtenção de informações básicas sobre um Pokémon existente.
*test_validacao_dados.py*: Valida se as informações dos Pokémons estão corretas, como nome, ID e base_experience.



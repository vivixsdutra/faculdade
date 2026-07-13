from pokedex import Pokedex
from helper.WriteAJson import writeAJson

# Inicializando a Pokedex
pokedex = Pokedex(database="pokedex", collection="pokemons")

# Resetando o banco de dados
pokedex.database.resetDatabase()

# Todos os pokemons
pokemons = pokedex.get_all_pokemons()

# Pokemon por nome
pikachu = pokedex.get_pokemon_by_name("Pikachu")

# Pokemon por tipo
types = ["Fighting"]
pokemons_by_type = pokedex.get_pokemons_by_type(types)

# Pokemons tipo grama OU veneno que tem evolução
tipos = ["Grass", "Poison"]
pokemons_with_evolution = pokedex.get_pokemons_with_evolution_by_type(tipos)

# Pokemons fracos contra psíquico E gelo
fraquezas = ["Psychic", "Ice"]
pokemons_weak_against_psychic_ice = pokedex.get_pokemons_weak_against(fraquezas)

# Pokemons que tem APENAS uma fraqueza
pokemons_with_one_weakness = pokedex.get_pokemons_with_one_weakness()

# Pokemons que tem chance de spawn ENTRE 0.3 e 0.6
pokemons_spawn_chance = pokedex.get_pokemons_by_spawn_chance(0.3, 0.6)

# Pokemons que NÃO tem o campo multipliers ou ele é None/null
pokemons_no_multipliers = pokedex.get_pokemons_without_multipliers()

# Pokemons SEM o campo multipliers
pokemons_without_multipliers_field = pokedex.get_pokemons_without_multipliers_field()

# Pokemons que a segunda evolução aparece ATÉ o #021 da pokédex
pokemons_second_evolution = pokedex.get_pokemons_with_second_evolution("020")

# Pokémons que são de fogo OU fracos contra fogo
pokemons_fire_or_weak_against_fire = pokedex.get_pokemons_of_fire_or_weak_against_fire()

# Encerrando a conexão com o banco de dados
pokedex.close()

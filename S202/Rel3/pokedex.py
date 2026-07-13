from database import Database

class Pokedex:
    def __init__(self, database, collection):
        self.database = Database(database, collection)

    def log_result(self, filename, data):
        self.database.writeAJson(filename, data)

    def get_all_pokemons(self):
        result = list(self.database.collection.find())
        self.log_result('all_pokemons.json', result)
        return result

    def get_pokemon_by_name(self, name):
        query = {"name": name}
        result = list(self.database.collection.find(query))
        self.log_result('pokemon_by_name.json', result)
        return result

    def get_pokemons_by_type(self, types):
        query = {"type": {"$in": types}}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_by_type.json', result)
        return result

    def get_pokemons_with_evolution_by_type(self, types):
        query = {"type": {"$in": types}, "next_evolution": {"$exists": True}}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_with_evolution_by_type.json', result)
        return result

    def get_pokemons_weak_against(self, weaknesses):
        query = {"weaknesses": {"$all": weaknesses}}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_weak_against.json', result)
        return result

    def get_pokemons_with_one_weakness(self):
        query = {"weaknesses": {"$size": 1}}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_with_one_weakness.json', result)
        return result

    def get_pokemons_by_spawn_chance(self, min_chance, max_chance):
        query = {"spawn_chance": {"$gt": min_chance, "$lt": max_chance}}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_by_spawn_chance.json', result)
        return result

    def get_pokemons_without_multipliers(self):
        query = {"multipliers": None}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_without_multipliers.json', result)
        return result

    def get_pokemons_without_multipliers_field(self):
        query = {"multipliers": {"$exists": False}}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_without_multipliers_field.json', result)
        return result

    def get_pokemons_with_second_evolution(self, max_num):
        query = {"next_evolution.1.num": {"$lte": max_num}}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_with_second_evolution.json', result)
        return result

    def get_pokemons_of_fire_or_weak_against_fire(self):
        query = {"$or": [{"type": "Fire"}, {"weaknesses": "Fire"}]}
        result = list(self.database.collection.find(query))
        self.log_result('pokemons_of_fire_or_weak_against_fire.json', result)
        return result

    def close(self):
        self.database.clusterConnection.close()

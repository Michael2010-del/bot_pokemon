from random import randint
import requests

class Pokemon:
    pokemons = {}
    
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1, 1000)
        
        
        self._load_pokemon_data()
        
        Pokemon.pokemons[pokemon_trainer] = self
    
    def _load_pokemon_data(self):
        """Загружает все данные покемона за один запрос"""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Картинка
            self.img = data['sprites']['other']['official-artwork']['front_default']
            
            # Имя
            self.name = data['forms'][0]['name']
            
            # Типы (может быть несколько)
            self.types = [type_info['type']['name'] for type_info in data['types']]
            
            # Рост и вес 
            self.height = data["height"] / 10  
            self.weight = data["weight"] / 10  
            
            
        else:
            # Значения по умолчанию при ошибке
            self._set_default_values()
    
    def _set_default_values(self):
        """Устанавливает значения по умолчанию"""
        self.img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
        self.name = "Pikachu"
        self.types = ["electric"]
        self.height = 0.4  
        self.weight = 6.0  
        
    
    def info(self):
        types_str = ", ".join(self.types)
        return f"""
        🏷️ Имя: {self.name.capitalize()}
        👤 Тренер: {self.pokemon_trainer}
        ⚡ Тип(ы): {types_str}
        📏 Рост: {self.height} м
        ⚖️ Вес: {self.weight} кг
        """
    
    def show_img(self):
        return self.img
    
    def get_type(self):
        """Возвращает основной тип покемона"""
        return self.types[0] if self.types else "Universal"
    
    def get_all_types(self):
        """Возвращает все типы покемона"""
        return self.types
    
    def get_weight_height(self):
        """Возвращает рост и вес"""
        return {"height": self.height, "weight": self.weight}
    
    
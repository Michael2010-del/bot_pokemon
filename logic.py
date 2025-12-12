from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
        pokemons = {}
        # Инициализация объекта (конструктор)
        def __init__(self, pokemon_trainer):

            self.pokemon_trainer = pokemon_trainer   

            self.pokemon_number = randint(1,1000)
            self.img = self.get_img()
            self.name = self.get_name()

            self.hp = randint(10,100)
            self.power = randint(10,100)
            self.last_feed_time = datetime.now()
            Pokemon.pokemons[pokemon_trainer] = self

        # Метод для получения картинки покемона через API
        def get_img(self):
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return (data['sprites']['other']['official-artwork']['front_default'])
            else:
                return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"
        
        
        # Метод для получения имени покемона через API
        def get_name(self):
            url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return (data['forms'][0]['name'])
            else:
                return "Pikachu"


        # Метод класса для получения информации
        def info(self):
            return f"""Имя твоего покеомона: {self.name}
                    Здоровье: {self.hp}
                    Сила: {self.power}"""
        
        #Метод для кормления покемонов
        def feed(self, feed_interval=20, hp_increase=10):
                current_time = datetime.now()
                next_feed_time = self.last_feed_time + timedelta(seconds=feed_interval)
                if current_time >= next_feed_time:
                    self.hp += hp_increase
                    self.last_feed_time = current_time
                    return f"Покемон покормлен! Здоровье увеличено. Текущее здоровье: {self.hp}"
                else:
                    time_left = next_feed_time - current_time
                    return f"Рано кормить! Следующее кормление через: {time_left.seconds} секунд"

        # Метод класса для получения картинки покемона
        def show_img(self):
            return self.img
        
        def attack(self, enemy):
            if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
                chance = randint(1,5)
                if chance == 1:
                    return "Покемон-волшебник применил щит в сражении"

            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
            else:
                enemy.hp = 0
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


class Wizard(Pokemon):
        def attack(self, enemy):
            return super().attack(enemy)
        def feed(self):
             return super().feed(hp_increase=20)

class Fighter(Pokemon):
        def attack(self, enemy):
            super_power = randint(5,15)
            self.power += super_power
            result = super().attack(enemy)
            self.power -= super_power
            return result + f"\nБоец применил супер-атаку силой:{super_power} "
        def feed(self):
             return super().feed(feed_interval=10)
        


wizard = Wizard("username1")
fighter = Fighter("username2")

print(wizard.info())
print("#"*10)   
print(fighter.info())
print("#"*10)
print(wizard.attack(fighter))
print(fighter.attack(wizard))








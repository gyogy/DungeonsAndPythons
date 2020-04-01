class Soul():

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self):
        pass

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing):
        
        self.health += healing
        if self.health > health:
            self.health = health

    def take_mana(self, rest):

        self.mana += rest
        if self.mana > mana:
            self.mana = mana

    def attack(self, by):
        pass

    def take_damage(self, damage):

        self.health -= damage
        if self.health < 0:
            self.health = 0


class Hero(Soul):
    
    def __init__(self, name, title, health, mana, mana_regen_rate)
        super().__init__(name)
        self.title = title
        super().__init__(health)
        super().__init__(mana)
        self.mana_regen_rate = mana_regen_rate
        self.equipped_weapon = None
        self.learned_spell = None

    def known_as(self):
        return f'{self.name} the {self.title}'

    def equip(self, weapon):
        self.equipped_weapon = weapon

    def learn(self, spell):
        self.learned_spell = spell

class Enemy(Soul):
    pass

class Weapon():
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Spell():

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

class Dungeon():

    def __init__(self, map_path):
        self.map = load_map(map_path)
        self.treasure_on_map = []
        self.hero = None
        self.hero_position = 0

    def load_map(self, map_path):
        pass

    def print_map(self):
        pass

    def spawn(self, hero):
        pass

    def move_hero(self):
        pass

    def pick_treasure(self):
        pass

    def hero_attack(self, by):
        pass

class Fight():

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
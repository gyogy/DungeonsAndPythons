class Soul():

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        pass

    def can_cast(self):
        pass

    def get_health(self):
        pass

    def get_mana(self):
        pass

    def take_healing(self):
        pass

    def take_mana(self):
        pass

    def attack(self, by):
        pass

    def take_damage(self, damage):
        pass


class Hero(Soul):
    
    def __init__(self, name, title, health, mana, mana_regen_rate)
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regen_rate = mana_regen_rate
        self.equipped_weapon = ''
        self.learned_spell

    def known_as(self):
        pass

    def equip(self, weapon):
        pass

    def learn(self, spell):
        pass

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
from dungeons_utils import load_map

class Soul():

    def __init__(self, health, mana, damage=0):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.weapon = None
        self.spell = None

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self):
        if self.spell is None:
            return False
        elif self.spell.mana_cost > self.mana:
            return False
        else:
            return True

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing):
        if self.health > 0:

            self.health += healing
            if self.health > health:
                self.health = health
            return True

        else:
            return False

    def take_mana(self, rest):

        self.mana += rest
        if self.mana > mana:
            self.mana = mana

    def attack(self, by=''):
        if by == 'weapon' and self.weapon is not None:
            return self.weapon.damage
        
        elif by == 'magic' and self.spell is not None:
            return self.spell.damage

        else:
            return self.damage

    def take_damage(self, damage):

        self.health -= damage
        if self.health < 0:
            self.health = 0


class Hero(Soul):
    
    def __init__(self, name, title, health, mana, mana_regen_rate):
        self.name = name
        self.title = title
        super().__init__(health, mana)
        self.mana_regen_rate = mana_regen_rate

    def known_as(self):
        return f'{self.name} the {self.title}'

class Enemy(Soul):
    
    def __init__(self, health, mana, damage):
        super().__init__(health, mana, damage)

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
        self.enemies_on_map = []
        self.hero = None
        self.hero_position = ()

    def print_map(self):
        for level in self.map:
            print(''.join(level))

    def spawn(self, hero):
        # TODO: test if hero is Hero instance
        self.hero = hero

        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[0])):
                if self.map[i][j] == 'S':
                    self.hero_position = (i,j)
                    self.map[i][j] = 'H'
                    return True
        # When Hero moves from a square it becomes '.'
        return False

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


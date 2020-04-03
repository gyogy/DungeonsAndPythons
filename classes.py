from dungeons_utils import load_map, load_treasures
import random

class Soul():

    def __init__(self, health, mana, damage=0):
        #Added current_mana and current_health
        self.health = health
        self.current_health = health
        self.mana = mana
        self.current_mana = mana
        self.damage = damage
        self.weapon = None
        self.spell = None

    def is_alive(self):
        if self.current_health > 0:
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
        return self.current_health

    def get_mana(self):
        return self.current_mana

    def take_healing(self, healing):
        if self.current_health > 0:
            # Made changes
            self.current_health += healing
            if self.current_health > self.health:
                self.current_health = self.health
            return True

        else:
            return False

    def take_mana(self, rest):
        # Mada changes
        self.current_mana += rest
        if self.current_mana > self.mana:
            self.current_mana = self.mana

    def attack(self, by=''):
        if by == 'weapon' and self.weapon is not None:
            return self.weapon.damage
        
        elif by == 'magic' and self.spell is not None:
            return self.spell.damage

        else:
            return self.damage

    def take_damage(self, damage):

        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0


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
        self.treasure_on_map = load_treasures(map_path)
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

    def move_hero(self, direction):
        if direction == 'up':
            self.move_up()
        elif direction == 'down':
            self.move_down()
        elif direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()
        else:
            raise ValueError('Invalid direction')

    def move_up(self):
        # future hero position 
        fhp = (self.hero_position[0]-1,self.hero_position[1])
        
        if fhp[0] < 0:
            return False
        elif self.map[fhp[0]][fhp[1]] == '.':
            self.map[fhp[0]][fhp[1]] = 'H'
            self.map[fhp[0]+1][fhp[1]] = '.'
            self.hero_position = fhp
            self.hero.take_mana(self.hero.mana_regen_rate)
            return True
        elif self.map[fhp[0]][fhp[1]] == '#':
            return False
        elif self.map[fhp[0]][fhp[1]] == 'E':
            # start fight
            pass
        elif self.map[fhp[0]][fhp[1]] == 'G':
            print('Congratulations you have sucessfully make it throught this level')
        else:
            self.pick_treasure()
            self.map[fhp[0]+1][fhp[1]] = '.'
            self.map[fhp[0]][fhp[1]] = 'H'
            self.hero_position = fhp
            self.hero.take_mana(self.hero.mana_regen_rate)
            pass


    def move_down(self):
        fhp = (self.hero_position[0]+1,self.hero_position[1])
        
        if fhp[0] > len(self.map) - 1 :
            return False
        elif self.map[fhp[0]][fhp[1]] == '.':
            self.map[fhp[0]][fhp[1]] = 'H'
            self.map[fhp[0]-1][fhp[1]] = '.'
            self.hero_position = fhp
            self.hero.take_mana(self.hero.mana_regen_rate)
            return True
        elif self.map[fhp[0]][fhp[1]] == '#':
            return False
        elif self.map[fhp[0]][fhp[1]] == 'G':
            print('Congratulations you have sucessfully make it throught this level')
        elif self.map[fhp[0]][fhp[1]] == 'E':
            # start fight
            pass
        else:
            self.pick_treasure()
            self.map[fhp[0]-1][fhp[1]] = '.'
            self.map[fhp[0]][fhp[1]] = 'H'
            self.hero_position = fhp
            self.hero.take_mana(self.hero.mana_regen_rate)

    def move_left(self):
        fhp = (self.hero_position[0],self.hero_position[1]-1)
        print(self.map[fhp[0]][fhp[1]])
        if fhp[1] < 0:
            return False
        elif self.map[fhp[0]][fhp[1]] == '.':
            self.map[fhp[0]][fhp[1]] = 'H'
            self.map[fhp[0]][fhp[1]+1] = '.'
            self.hero_position = fhp
            self.hero.take_mana(self.hero.mana_regen_rate)
            return True
        elif self.map[fhp[0]][fhp[1]] == 'G':
            print('Congratulations you have sucessfully make it throught this level')
        elif self.map[fhp[0]][fhp[1]] == '#':
            return False
        elif self.map[fhp[0]][fhp[1]] == 'E':
            # start fight
            pass
        else:
            self.pick_treasure()
            self.map[fhp[0]][fhp[1]+1] = '.'
            self.map[fhp[0]][fhp[1]] = 'H'
            self.hero_position = fhp
            self.hero.take_mana(self.hero.mana_regen_rate)

    def move_right(self):
        fhp = (self.hero_position[0], self.hero_position[1]+1)
        
        if fhp[1] > len(self.map) - 1 :
            return False
        elif self.map[fhp[0]][fhp[1]] == '.':
            self.map[fhp[0]][fhp[1]] = 'H'
            self.map[fhp[0]][fhp[1]-1] = '.'
            self.hero_position = fhp
            return True
        elif self.map[fhp[0]][fhp[1]] == '#':
            return False
        elif self.map[fhp[0]][fhp[1]] == 'G':
            print('Congratulations you have sucessfully make it throught this level')
        elif self.map[fhp[0]][fhp[1]] == 'E':
            # start fight
            pass
        else:
            self.pick_treasure()
            self.map[fhp[0]][fhp[1]-1] = '.'
            self.map[fhp[0]][fhp[1]] = 'H'
            self.hero_position = fhp
            self.hero.take_mana(self.hero.mana_regen_rate)


    def pick_treasure(self):
        treasure = random.choice(self.treasure_on_map)

        if treasure[0] == 'Spell':
            print(f'New spell learned: {treasure[1]}')
            self.hero.learn(Spell(treasure[1],int(treasure[2]),int(treasure[3]),int(treasure[4])))
        elif treasure[0] == 'Weapon':
            print(f'New weapon equiped: {treasure[1]}')
            self.hero.equip(Weapon(treasure[1],int(treasure[2])))
        elif treasure[0] == 'Heal':
            print(f'Heal potion found! +{treasure[1]}hp')
            self.hero.take_healing(int(treasure[1]))
        elif treasure[0] == 'Mana':
            print(f'Mana potion found! +{treasure[1]}mana')
            self.hero.take_mana(int(treasure[1]))
        else:
            raise ValueError('Invalid treasure type')

    def hero_attack(self, by):
        pass

class Fight():

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy



import unittest
from classes import *

weapon = Weapon('Sword of Bad Manners', 20)
spell = Spell('Fireball', 20, 100, 3)

pesho = Hero('Pesho', 'Koftito', 100, 100, 2)
pesho.equip(weapon)
pesho.learn(spell)

vrago = Enemy(60, 100, 20)


class TestHeroClass(unittest.TestCase):

    def test_attacking_with_spell_decreasing_current_mana(self):
        pesho.attack(by='magic')
        pesho.attack(by='magic')
        pesho.attack(by='magic')

        result = pesho.current_mana
        expected = 0

        self.assertEqual(result, expected)


class TestFightClass(unittest.TestCase):

    def test_fight_init(self):
        kopon = Fight(pesho, vrago)

        result = kopon.commence()
        expected = True
        # if kopon.commence() returns True, hero has defeated enemy

        self.assertEqual(result, expected)


class TestDungeonClass(unittest.TestCase):

    def test_a_fight_started_going_right_range_1(self):
        d = Dungeon('levels/level0.txt')
        gosho = Hero('Gosho', 'Tupoto', 40, 10, 2)
        d.spawn(gosho)
        d.move_hero('right')
        d.move_hero('right')
        d.move_hero('right')
        d.move_hero('right')
        d.move_hero('right')

        result = d.hero.current_health
        expected = 20

        self.assertEqual(result, expected)

    def test_a_fight_started_going_down_range_1(self):
        d = Dungeon('levels/level00.txt')
        tosho = Hero('Tosho', 'Ostroto', 40, 10, 2)
        d.spawn(tosho)
        d.move_hero('down')
        d.move_hero('down')

        result = d.hero.is_alive()
        expected = False

        self.assertEqual(result, expected)

    def test_a_fight_started_going_up_range_1(self):
        d = Dungeon('levels/level000.txt')
        losho = Hero('Losho', 'Koftito', 40, 10, 2)
        d.spawn(losho)
        d.move_hero('up')
        d.move_hero('up')

        result = d.hero.is_alive()
        expected = False

        self.assertEqual(result, expected)

    def test_a_fight_started_going_left_range_1(self):
        d = Dungeon('levels/level0000.txt')
        sasho = Hero('Sasho', 'Sushata', 40, 10, 2)
        d.spawn(sasho)
        d.move_hero('left')
        d.move_hero('left')

        result = d.hero.is_alive()
        expected = False

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

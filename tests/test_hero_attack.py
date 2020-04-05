import unittest
from classes import *


class TestDungeonClass(unittest.TestCase):

    def test_hero_attack_out_of_range(self):
        d = Dungeon('levels/levelZ.txt')
        s = Spell('Icebolt', 10, 10, 2)
        gosho = Hero('Gosho', 'Tupoto', 40, 20, 2)
        gosho.learn(s)
        d.spawn(gosho)

        result = d.hero_attack(by='magic', direction='right')
        expected = 'Noone in range.'

        self.assertEqual(result, expected)

    def test_hero_attack_without_knowing_a_spell(self):
        d = Dungeon('levels/levelZ.txt')
        gosho = Hero('Gosho', 'Tupoto', 40, 20, 2)
        d.spawn(gosho)
        d.move_hero('right')

        result = d.hero_attack(by='magic', direction='right')
        expected = 'Gosho doesn\'t know any spells.'

        self.assertEqual(result, expected)

    def test_hero_attack_to_the_right_from_range_2(self):
        d = Dungeon('levels/levelZ.txt')
        s = Spell('Icebolt', 10, 10, 2)
        w = Weapon('Machete', 20)
        gosho = Hero('Gosho', 'Tupoto', 40, 20, 2)
        gosho.learn(s)
        gosho.equip(w)
        d.spawn(gosho)
        d.move_hero('right')

        result = d.hero_attack(by='magic', direction='right')
        expected = True

        self.assertEqual(result, expected)

    def test_hero_attack_down_from_range_2(self):
        d = Dungeon('levels/level00.txt')
        s = Spell('Icebolt', 10, 10, 2)
        w = Weapon('Machete', 20)
        gosho = Hero('Gosho', 'Tupoto', 40, 20, 2)
        gosho.learn(s)
        gosho.equip(w)
        d.spawn(gosho)

        result = d.hero_attack(by='magic', direction='down')
        expected = True

        self.assertEqual(result, expected)

    def test_hero_attack_left_from_range_2(self):
        d = Dungeon('levels/level0000.txt')
        s = Spell('Icebolt', 10, 10, 2)
        w = Weapon('Machete', 20)
        gosho = Hero('Gosho', 'Tupoto', 40, 20, 2)
        gosho.learn(s)
        gosho.equip(w)
        d.spawn(gosho)

        result = d.hero_attack(by='magic', direction='left')
        expected = True

        self.assertEqual(result, expected)

    def test_hero_attack_up_from_range_2(self):
        d = Dungeon('levels/level000.txt')
        s = Spell('Icebolt', 10, 10, 2)
        w = Weapon('Machete', 20)
        gosho = Hero('Gosho', 'Tupoto', 40, 20, 2)
        gosho.learn(s)
        gosho.equip(w)
        d.spawn(gosho)

        result = d.hero_attack(by='magic', direction='up')
        expected = True

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

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
        expected = 'He ded.'

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

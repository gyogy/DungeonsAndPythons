import unittest
from classes import Hero, Enemy, Weapon, Spell

pesho = Hero('Petr', 'Pedo', 100, 100, 2)
vrago = Enemy(100, 100, 20)
weapon = Weapon('Sword of Bad Manners', 20)
spell = Spell('Fireball', 60, 100, 3)


class TestHeroClass(unittest.TestCase):

    def test_hero_init(self):
        result = pesho.health
        expected = 100

        self.assertEqual(result, expected)

    def test_hero_take_damage_and_is_alive(self):
        pesho.take_damage(100)

        result = pesho.is_alive()
        expected = False

        self.assertEqual(result, expected)

    def test_hero_take_damage_and_get_health(self):
        pesho.take_damage(57)

        result = pesho.get_health()
        expected = 43

        self.assertEqual(result, expected)

    def test_hero_can_cast(self):
        pesho.learn(spell)

        result = pesho.can_cast()
        expected = True

        self.assertEqual(result, expected)

    def test_hero_can_cast_when_no_spell_is_learned(self):
        pesho.spell = None

        result = pesho.can_cast()
        expected = False

        self.assertEqual(result, expected)


class TestEnenmyClass(unittest.TestCase):

    def test_unequipped_enemys_attack_method(self):

        result = vrago.attack(by='magic')
        expected = 20

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

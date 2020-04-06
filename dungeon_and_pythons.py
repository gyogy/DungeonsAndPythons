from classes import *


def main():
    dungeon = Dungeon('levels/level0.txt')
    dungeon.print_map()
    dungeon.spawn(Hero('Niki', 'We', 100, 100, 5))
    dungeon.move_right()
    dungeon.move_right()
    dungeon.print_map()
    dungeon.hero.learn(Spell('CannonBall', 20, 10, 5))
    dungeon.hero_attack(by='magic')
    dungeon.print_map()


if __name__ == '__main__':
    main()

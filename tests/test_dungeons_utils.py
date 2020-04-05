import unittest
from dungeons_utils import (
    split_line,
    load_map,
    load_treasures,
    check_if_dungeon_map_has_forbidden_symbols,
    load_enemies)


class TestSplitLine(unittest.TestCase):
    def test_with_empty_string_should_return_empty_list(self):
        input = ''
        wanted_result = []

        result = split_line(input)

        self.assertEqual(wanted_result, result)

    def test_with_correct_input(self):
        input = 'T...#'
        wanted_result = ['T', '.', '.', '.', '#']

        result = split_line(input)

        self.assertEqual(wanted_result, result)


class TestLoadMap(unittest.TestCase):
    def test_with_file_that_is_not_correctly_set(self):
        # If there is not --Treasures after the map
        exc = None

        try:
            load_map('files_for_tests/test_with_file_that_is_not_correctly_set.txt')
        except ValueError as err:
            exc = err
        self.assertIsNotNone(exc)

    def test_with_correct_file_that_is_correctly_set(self):
        wanted_result = [['S', '.', '.', '#', '.'], ['S', '.', '.', 'T', '.']]

        result = load_map('files_for_tests/test_with_correct_file_that_is_correctly_set.txt')
        self.assertEqual(wanted_result, result)


class TestLoadTreasures(unittest.TestCase):
    def test_with_file_that_is_incorrectly_set(self):
        # if there is not --Treasures after the map and no --Enemies after the treasures
        exc = None

        try:
            load_treasures('files_for_tests/test_with_file_that_is_incorrectly_set.txt')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Incorrect format of file(No --Treasures)')

    def test_with_file_that_doesnt_have_enemies_line(self):
        exc = None

        try:
            load_treasures('files_for_tests/test_with_file_that_doesnt_have_enemies_line.txt')
        except Exception as err:
            exc = err

        self.assertEqual(str(exc), 'Incorrect format of file(No --Enemies)')
        self.assertIsNotNone(exc)

    def test_with_files_that_has_enemies_and_treasures(self):
        wanted_result = [['Spell', 'Fireball', '10', '2', '4\n'], ['Weapon', 'Axe', '4\n']]

        result = load_treasures('files_for_tests/test_with_files_that_has_enemies_and_treasures.txt')

        self.assertEqual(wanted_result, result)


class TestCheckIfDungeonMapHasForbiddenSymbols(unittest.TestCase):
    def test_with_wrong_input(self):
        input = [['.', '#', 'G', 'S'], ['.', '.', '.', ','], ['H', 'E', 'T', 'T']]
        exc = None

        try:
            check_if_dungeon_map_has_forbidden_symbols(input)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_with_correct_input(self):
        input = [['.', '#', 'T', 'E', 'H', 'G']]

        result = check_if_dungeon_map_has_forbidden_symbols(input)

        self.assertTrue(result)


class TestLoadEnemies(unittest.TestCase):
    def test_with_file_that_doesnt_have_enemies(self):
        exc = None

        try:
            load_enemies('files_for_tests/test_with_file_that_doesnt_have_enemies.txt')
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_with_file_that_doesnt_have_eog_line(self):
        exc = None

        try:
            load_enemies('files_for_tests/test_with_file_that_doesnt_have_eog_line.txt')
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_with_file_that_is_correct(self):
        wanted_result = [['Enemy', '10', '20', '20\n'], ['Enemy', '30', '40', '20\n'], ['Enemy', '50', '30', '20\n']]

        result = load_enemies('files_for_tests/test_with_file_that_is_correct.txt')

        self.assertEqual(wanted_result, result)


if __name__ == '__m1in__':
    unittest.main()

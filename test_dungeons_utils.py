import unittest
from dungeons_utils import split_line, load_map, load_treasures

class TestSplitLine(unittest.TestCase):
    def test_with_empty_string_should_return_empty_list(self):
        input = ''
        wanted_result = []

        result = split_line(input)

        self.assertEqual(wanted_result, result)

    def test_with_correct_input(self):
        input = 'T...#'
        wanted_result = ['T','.','.','.','#']

        result = split_line(input)

        self.assertEqual(wanted_result, result)

class TestLoadMap(unittest.TestCase):
    def test_with_file_that_is_not_correctly_set(self):
        # If there is not --Treasures after the map
        file = open('files_for_tests/test_with_file_that_is_not_correctly_set.txt', 'r')
        exc = None

        try:
            load_map('files_for_tests/test_with_file_that_is_not_correctly_set.txt')
        except ValueError as err:
            exc = err
        file.close()
        self.assertIsNotNone(exc)

    def test_with_correct_file_that_is_correctly_set(self):
        file = open('files_for_tests/test_with_correct_file_that_is_correctly_set.txt','r')
        wanted_result = [['S','.','.','#','.'],['S','.','.','T','.']]

        result = load_map('files_for_tests/test_with_correct_file_that_is_correctly_set.txt')
        file.close()
        self.assertEqual(wanted_result, result)

class TestLoadTreasures(unittest.TestCase):
    def test_with_file_that_is_incorrectly_set(self):
        # if there is not --Treasures after the map and no --Enemies after the treasures
        file = open('files_for_tests/test_with_file_that_is_incorrectly_set.txt','r')
        exc = None

        try:
            load_treasures('files_for_tests/test_with_file_that_is_incorrectly_set.txt')
        except Exception as err:
            exc = err

        file.close()
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect format of file(No --Treasures)')

    def test_with_file_that_doesnt_have_enemies_line(self):
        file = open('files_for_tests/test_with_file_that_doesnt_have_enemies_line.txt','r')
        exc = None

        try:
            load_treasures('files_for_tests/test_with_file_that_doesnt_have_enemies_line.txt')
        except Exception as err:
            exc = err

        file.close()
        self.assertEqual(str(exc),'Incorrect format of file(No --Enemies)')
        self.assertIsNotNone(exc)

    def test_with_files_that_has_enemies_and_treasures(self):
        file = open('files_for_tests/test_with_files_that_has_enemies_and_treasures.txt','r')
        wanted_result = [['Spell','Fireball','10','2','4\n'],['Weapon','Axe','4\n']]
        
        result = load_treasures('files_for_tests/test_with_files_that_has_enemies_and_treasures.txt')
        file.close()
        
        self.assertEqual(wanted_result, result)

if __name__ == '__main__':
    unittest.main()
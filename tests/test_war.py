import unittest
from unittest import TestCase

from tame_of_thrones.kingdom import Kingdom
from tame_of_thrones.war import War


class TestWar(TestCase):

    def test_get_character_count_map_of_lowercase_string(self):
        self.assertDictEqual({'a': 1, 'c': 3, 'b': 2}, War.get_character_count_map("abccbc"))

    def test_get_character_count_map_of_uppercase_string(self):
        self.assertDictEqual({'p': 1, 'q': 2, 'r': 3}, War.get_character_count_map("RRRQQP"))

    def test_get_character_count_map_of_mixed_case_string(self):
        self.assertDictEqual({'p': 1, 'q': 2, 'r': 3}, War.get_character_count_map("RrrQqp"))

    def test_result_win(self):
        kingdom_1 = Kingdom('LAND', 'PANDA')
        self.assertTrue(War.get_war_result(kingdom_1, 'FDIXXSOKKOFBBMU'))

    def test_result_loss(self):
        kingdom_1 = Kingdom('LAND', 'PANDA')
        self.assertFalse(War.get_war_result(kingdom_1, 'PANDA'))


if __name__ == "__main__":
    unittest.main()

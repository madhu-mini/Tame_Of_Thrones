import unittest
from unittest import TestCase

from Kingdom import Kingdom
from War import War


class TestWar(TestCase):

    def test_get_mapping_lowercase_string(self):
        self.assertDictEqual({'a': 1, 'c': 3, 'b': 2}, War.getMapping("abccbc"))

    def test_get_mapping_uppercase_string(self):
        self.assertDictEqual({'p': 1, 'q': 2, 'r': 3}, War.getMapping("RRRQQP"))

    def test_get_mapping_mixed_case_string(self):
        self.assertDictEqual({'p': 1, 'q': 2, 'r': 3}, War.getMapping("RrrQqp"))

    def test_result_win(self):
        kingdom_1 = Kingdom('LAND', 'PANDA')
        self.assertTrue(War.result(kingdom_1, 'FDIXXSOKKOFBBMU'))

    def test_result_loss(self):
        kingdom_1 = Kingdom('LAND', 'PANDA')
        self.assertFalse(War.result(kingdom_1, 'PANDA'))


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest import TestCase

from tame_of_thrones.kingdom import Kingdom
from tame_of_thrones.exceptions.universeExceptions import InvalidKingdomError


class TestKingdom(TestCase):

    def test_kingdom_with_no_name(self):
        kingdom_name = None
        kingdom_emblem = 'panda'
        self.assertRaises(InvalidKingdomError, Kingdom, kingdom_name, kingdom_emblem)

    def test_kingdom_with_empty_name(self):
        kingdom_name = ''
        kingdom_emblem = 'panda'
        self.assertRaises(InvalidKingdomError, Kingdom, kingdom_name, kingdom_emblem)

    def test_kingdom_with_no_emblem(self):
        kingdom_name = 'Maharashtra'
        kingdom_emblem = 'panda'
        self.assertRaises(InvalidKingdomError, Kingdom, kingdom_name, kingdom_emblem)

    def test_emblem_with_no_name(self):
        kingdom_name = 'Space'
        kingdom_emblem = None
        self.assertRaises(InvalidKingdomError, Kingdom, kingdom_name, kingdom_emblem)

    def test_emblem_with_empty_name(self):
        kingdom_name = 'Space'
        kingdom_emblem = ''
        self.assertRaises(InvalidKingdomError, Kingdom, kingdom_name, kingdom_emblem)

    def test_emblem_with_not_existing_kingdom(self):
        kingdom_name = 'Space'
        kingdom_emblem = 'coconut'
        self.assertRaises(InvalidKingdomError, Kingdom, kingdom_name, kingdom_emblem)

    # To check whether kingdom object is created or not
    def test_create_kingdom_without_king(self):
        kingdom_name = 'SPACE'
        kingdom_emblem = 'Gorilla'
        self.assertIsInstance(Kingdom(kingdom_name, kingdom_emblem), Kingdom)

    # To check whether kingdom object is created or not
    def test_create_kingdom_with_king(self):
        kingdom_name = 'SPACE'
        kingdom_emblem = 'Gorilla'
        king_name = 'King Shan'
        self.assertIsInstance(Kingdom(kingdom_name, kingdom_emblem, king_name), Kingdom)


if __name__ == "__main__":
    unittest.main()

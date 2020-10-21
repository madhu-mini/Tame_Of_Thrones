from unittest import TestCase

from tame_of_thrones.universe import Universe
from tame_of_thrones.exceptions.universe_exceptions import InvalidUniverseError


class TestUniverse(TestCase):

    def test_universe_with_no_reigns(self):
        reigns = None
        self.assertRaises(InvalidUniverseError, Universe, reigns)

    def test_universe_with_empty_reigns(self):
        reigns = ''
        self.assertRaises(InvalidUniverseError, Universe, reigns)

    def test_universe_with_unknown_reigns(self):
        reigns = 'India'
        self.assertRaises(InvalidUniverseError, Universe, reigns)

    # To check whether kingdom object is created or not
    def test_create_universe(self):
        reigns = 'Southeros'
        self.assertIsInstance(Universe(reigns), Universe)

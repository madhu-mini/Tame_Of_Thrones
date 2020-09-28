from unittest import TestCase

from Universe import Universe
from Universe_Exceptions import InvalidUniverseException


class TestUniverse(TestCase):

    def test_universe_with_no_reigns(self):
        reigns = None
        self.assertRaises(InvalidUniverseException, Universe, reigns)

    def test_universe_with_empty_reigns(self):
        reigns = ''
        self.assertRaises(InvalidUniverseException, Universe, reigns)

    def test_universe_with_unknown_reigns(self):
        reigns = 'India'
        self.assertRaises(InvalidUniverseException, Universe, reigns)

    # To check whether kingdom object is created or not
    def test_create_universe(self):
        reigns = 'Southeros'
        self.assertIsInstance(Universe(reigns), Universe)

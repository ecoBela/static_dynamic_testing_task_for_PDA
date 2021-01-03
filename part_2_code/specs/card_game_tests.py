import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Clubs", 2)

    def test_card_has_value(self):
        self.assertEqual(2, self.card2.value)
    
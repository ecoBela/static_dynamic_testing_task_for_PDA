import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Clubs", 2)
        self.card3 = Card("Spades", 9)
        self.card4 = Card("Diamonds", 10)
        self.card_game1 = CardGame([self.card1])
        self.card_game2 = CardGame([self.card2])
        self.card_game3 = CardGame([self.card3, self.card4])

    def test_card_has_value(self):
        self.assertEqual(2, self.card2.value)
    
    def test_card_has_suit(self):
        self.assertEqual("Clubs", self.card1.suit)

    def test_card_game_has_cardlist(self):
        self.assertEqual([], self.card_game1.cardlist)
        self.assertEqual([], self.card_game3.cardlist)

    def test_check_for_ace(self):
        result = self.card_game1.check_for_ace(self.card1)
        result2 = self.card_game2.check_for_ace(self.card2)
        self.assertEqual(True, result)
        self.assertEqual(False, result2)

    
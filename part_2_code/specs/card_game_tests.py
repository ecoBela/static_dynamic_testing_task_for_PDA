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
        # result = self.card_game2.check_for_ace(self.card_game2.cardlist[0].value)
        # self.assertEqual(False, result)
        result = self.card_game1.check_for_ace(self.card1)
        result2 = self.card_game2.check_for_ace(self.card2)
        result3 = self.card_game1.check_for_ace(self.card2)
        result4 = self.card_game2.check_for_ace(self.card1)
        self.assertEqual(True, result)
        self.assertEqual(False, result2)
        self.assertEqual(False, result3)
        self.assertEqual(True, result4)

    def test_highest_card(self):
        result = self.card_game3.highest_card(self.card3, self.card4)
        self.assertEqual(self.card4, result)

    def test_cards_total(self):
        result = self.card_game3.cards_total([self.card4, self.card3])
        self.assertEqual(19, result)



    
import unittest

from poker.card import Card
from poker.validators import FullHouseValidator 

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven_of_diamonds  = Card("7", "Diamonds")
        self.seven_of_hearts    = Card("7", "Hearts")
        self.seven_of_spades    = Card("7", "Spades")
        self.ace_of_hearts      = Card("Ace", "Hearts")
        self.ace_of_spades      = Card("Ace", "Spades")

        self.cards = [
            Card("4", "Clubs"),
            self.seven_of_diamonds,
            self.seven_of_hearts,
            self.seven_of_spades,
            self.ace_of_hearts,
            self.ace_of_spades,
            Card("Queen", "Hearts")
        ]
    def test_validates_that_cards_have_two_of_the_same_rank_and_three_of_another_rank(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_cards_with_three_of_same_rank_and_two_of_same_rank(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_diamonds,
                self.seven_of_hearts,
                self.seven_of_spades,
                self.ace_of_hearts,
                self.ace_of_spades
            ]
        )
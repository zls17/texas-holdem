import unittest

from poker.card import Card
from poker.validators import TwoPairValidator 

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven_of_diamonds = Card("7", "Diamonds")
        self.seven_of_hearts = Card("7", "Hearts")
        self.eight_of_spades = Card("8", "Spades")
        self.ace_of_clubs = Card("Ace", "Clubs")
        self.ace_of_spades = Card("Ace", "Spades")            

        self.cards = [
            self.seven_of_diamonds,
            self.seven_of_hearts,
            self.eight_of_spades,
            self.ace_of_clubs,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_at_least_two_pairs_of_same_rank(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_diamonds,
                self.seven_of_hearts,
                self.ace_of_clubs,
                self.ace_of_spades
            ]
        )

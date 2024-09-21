import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven_of_spades = Card("7", "Spades")
        self.seven_of_diamonds = Card("7", "Diamonds")
        self.seven_of_hearts = Card("7", "Hearts")
        self.seven_of_clubs = Card("7", "Clubs")
        self.ace_of_spades = Card("Ace", "Spades")
    
        self.cards = [
            Card(rank = "5", suit = "Diamonds"),
            self.seven_of_clubs,
            self.seven_of_diamonds,
            self.seven_of_hearts,
            self.seven_of_spades,
            self.ace_of_spades,
            Card(rank = "Queen", suit = "Hearts")
        ]
        
    def test_validates_that_cards_have_four_of_the_same_rank(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_collection_with_four_of_same_rank(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_clubs,
                self.seven_of_diamonds,
                self.seven_of_hearts,
                self.seven_of_spades,
            ]
        )
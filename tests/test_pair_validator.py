import unittest

from poker.card import Card
from poker.validators import PairValidator 

class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_exactly_one_pair(self):
        cards = [
            Card("Ace", "Spades"),
            Card("Ace", "Clubs")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_pair_from_card_collection(self):
        ten_of_spades = Card("10", "Spades")
        ten_of_clubs = Card("10", "Clubs")
        cards = [
            Card("2", "Hearts"),
            Card("3", "Clubs"),
            ten_of_clubs,
            ten_of_spades,
            Card("King", "Diamonds")
        ]
        validator = PairValidator(cards = cards)
        self.assertEqual(
            validator.valid_cards(),
            [ten_of_clubs, ten_of_spades]
        )
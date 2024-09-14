import unittest

from poker.card import Card
from poker.validators import HighCardValidator 

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_high_card(self):
        cards = [
            Card("7", "Clubs"),
            Card("Ace", "Diamonds")
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_high_card_from_card_collection(self):
        ace = Card(rank = "Ace", suit = "Hearts")
        cards = [
            Card("5", "Spades"),
            Card("7", "Diamonds"),
            Card("9", "Clubs"),
            Card("10", "Clubs"),
            ace
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace]
        )
import unittest

from poker.card import Card
from poker.validators import StraightValidator 

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        three       = Card("3", "Clubs")
        six         = Card("6", "Hearts")
        self.seven  = Card("7", "Diamonds")
        self.eight  = Card("8", "Clubs")
        self.nine   = Card("9", "Spades")
        self.ten    = Card("10", "Spades")
        self.jack   = Card("Jack", "Diamonds")

        self.cards = [
            three,
            six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_determines_if_there_are_five_card_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven,
                self.eight,
                self.nine,
                self.ten,
                self.jack
            ]
        )
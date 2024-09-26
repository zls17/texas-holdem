import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.ten    = Card("10", "Spades")
        self.jack   = Card("Jack", "Spades")
        self.queen  = Card("Queen", "Spades")
        self.king   = Card("King", "Spades")
        self.ace    = Card("Ace", "Spades")

        self.cards = [
            Card("9", "Diamonds"),
            self.ten,
            self.jack,
            self.queen,
            self.king,
            self.ace,
            Card("Ace", "Diamonds")
        ]

    def test_validates_cards_do_not_have_straight_flush_ending_in_ace(self):
        self.cards.remove(self.ace)
        validator = RoyalFlushValidator(cards = self.cards)    
        self.assertEqual(
            validator.is_valid(),
            False 
        )        

    def test_validates_cards_have_straight_flush_ending_in_ace(self):
        validator = RoyalFlushValidator(cards = self.cards)    
    
        self.assertEqual(
            validator.is_valid(),
            True
        )        

    def test_returns_five_cards_with_straight_and_rank_ending_with_ace(self):
        validator = RoyalFlushValidator(cards = self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.ten,
                self.jack,
                self.queen,
                self.king,
                self.ace
            ]
        )

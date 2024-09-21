import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_determines_that_there_are_not_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            # is straight and flush but not straightflush
            Card("3", "Spades"),
            Card("4", "Spades"),
            Card("5", "Spades"),
            Card("6", "Spades"),
            Card("7", "Diamonds"),
            Card("King", "Spades"),
            Card("Ace", "Diamonds")
        ]
        
        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )     
    
    def test_determines_that_there_are_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card("3", "Spades"),
            Card("4", "Spades"),
            Card("5", "Spades"),
            Card("6", "Spades"),
            Card("7", "Spades"),
            Card("King", "Spades"),
            Card("Ace", "Diamonds")
        ]
        
        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )     

    def test_returns_collection_of_five_consecutive_cards_with_the_same_suit(self):
        three = Card("3", "Spades"),
        four  = Card("4", "Spades"),
        five  = Card("5", "Spades"),
        six   = Card("6", "Spades"),
        seven = Card("7", "Spades"),

        cards = [
            three,
            four,
            five,
            six,
            seven,
            Card("King", "Spades"),
            Card("Ace", "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                three,
                four,
                five,
                six,
                seven
            ]
        )

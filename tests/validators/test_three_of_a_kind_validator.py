import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        seven = Card("7", "Diamonds")
        eight = Card("8", "Spades")
        self.king_of_clubs = Card("King", "Clubs")
        self.king_of_hearts = Card("King", "Hearts")
        self.king_of_spades = Card("King", "Spades")
        self.cards = [
            seven,
            eight,
            self.king_of_clubs,
            self.king_of_hearts,
            self.king_of_spades
       ]
 
    def test_validates_that_cards_have_exactly_three_of_the_same_kind(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        
        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_three_of_a_kind_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [self.king_of_clubs, self.king_of_hearts, self.king_of_spades]
        )
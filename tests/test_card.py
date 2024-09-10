import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")
    
    def test_suit(self):
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_card_knows_its_rank_index(self):
        card = Card("Jack", "Hearts")
        self.assertEqual(card.rank_index, 9)

    def test_has_string_reprensentation_with_suit_and_rank(self):
        card = Card("7", "Diamonds")
        self.assertEqual(str(card), "7 of Diamonds")
    
    def test_has_technical_representation(self):
        card = Card("7", "Diamonds")
        self.assertEqual(repr(card), "Card('7', 'Diamonds')")
        
    def test_card_has_four_possible_suit_options(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )
    
    def test_card_has_thirteen_possible_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            (
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"
            )
        )
    
    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card("two", "Spades")
    
    def test_card_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card("2", "dots")
        
    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)

        self.assertEqual(
            cards[0],
            Card("2", "Hearts")
        )

        self.assertEqual(
            cards[-1],
            Card("Ace", "Diamonds")
        )
    
    def test_figures_out_if_two_cards_are_equal(self):
        self.assertEqual(
            Card("2", "Hearts"),
            Card("2", "Hearts")
        )
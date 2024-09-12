import unittest
from unittest.mock import patch
from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_has_length_equal_to_count_of_cards(self):
        deck = Deck()
        self.assertEqual(
            len(deck),
            0
        )
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_add_cards_to_its_collection(self):
        deck = Deck()
        card = Card("Ace", "Spades")
        deck.add_cards([card])
        self.assertEqual(deck.cards, [card])
    
    def test_removes_specified_number_of_cards_from_deck(self):
        ace = Card("Ace", "Spades"),
        eight = Card("8", "Hearts")
        cards = [
            ace,
            eight
        ]
        deck = Deck()
        deck.add_cards(cards = cards)
        
        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )

        self.assertEqual(
            deck.cards,
            [eight]
        )


    @patch("random.shuffle")
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        deck = Deck()
        cards = [
            Card("Ace", "Hearts"),
            Card("7", "Diamonds")
        ]
        deck.add_cards(cards)

        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)


        

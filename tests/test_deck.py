import unittest
from unittest.mock import patch
from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_add_cards_to_its_collection(self):
        deck = Deck()
        card = Card("Ace", "Spades")
        deck.add_cards([card])
        self.assertEqual(deck.cards, [card])

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


        

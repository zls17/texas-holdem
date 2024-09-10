import unittest
from poker.card import Card
from poker.hand import Hand 

class HandTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        cards = [Card("Ace", "Spades"),
                 Card("7", "Diamonds")]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.cards,
            cards
        )

    def test_figures_out_high_card_is_best_rank(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("7", "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )
    
    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card("Ace", "Spades"),
            Card("Ace", "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )


    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card("Ace", "Spades"),
            Card("Ace", "Clubs"),
            Card("7", "Hearts"),
            Card("7", "Diamonds"),
            Card("8", "Spades")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )
    
    def test_figures_out_three_of_a_kind(self):
        cards = [
            Card("King", "Hearts"),
            Card("King", "Spades"),
            Card("King", "Clubs"),
            Card("7", "Diamonds"),
            Card("8", "Spades")
        ]
    
        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )
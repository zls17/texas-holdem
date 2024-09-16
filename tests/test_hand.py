import unittest
from poker.card import Card
from poker.hand import Hand 

class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(
            hand.cards,
            []
        )
    
    def test_shows_all_its_card_in_technical_representation(self):
        cards = [
            Card("Ace", "Spades"),
            Card("Jack", "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            repr(hand),
            "Jack of Clubs, Ace of Spades"
        )

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card("Ace", "Spades")
        seven_of_diamonds = Card("7", "Diamonds")
        cards = [ace_of_spades, seven_of_diamonds]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [seven_of_diamonds, ace_of_spades]
        )

    def test_sort_two_cards_based_on_rank(self):
        
        king_of_diamonds = Card("King", "Diamonds")
        queen_of_hearts = Card("Queen", "Hearts")

        cards = [king_of_diamonds, queen_of_hearts]
        cards.sort()
        self.assertEqual(
            cards,
            [queen_of_hearts, king_of_diamonds]
        )
    
    def test_sort_five_cards_based_on_rank(self):
        ace_of_hearts = Card("Ace", "Hearts")
        five_of_diamonds = Card("5", "Diamonds")
        five_of_hearts = Card("5", "Hearts")
        three_of_clubs = Card("3", "Clubs")
        six_of_clubs = Card("6", "Clubs")
        
        unsorted_cards = [
            ace_of_hearts,
            five_of_hearts,
            five_of_diamonds,
            three_of_clubs,
            six_of_clubs
        ]

        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                three_of_clubs,
                five_of_diamonds,
                five_of_hearts,
                six_of_clubs,
                ace_of_hearts
            ]
        )
    
    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card("7", "Hearts"),
            Card("8", "Diamonds")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )
    
    def test_figures_out_best_rank_when_flush(self):
        cards = [
            Card(rank = rank, suit = "Hearts")
            for rank in ["2", "4", "7", "Jack", "Ace"]
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )
    
    def test_figures_out_full_house_is_best_rank(self):
        cards = [
            Card("7", "Spades"),
            Card("7", "Diamonds"),
            Card("7", "Hearts"),
            Card("Ace", "Hearts"),
            Card("Ace", "Spades")
        ]
        
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Full House"
        )

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card("7", "Spades"),
            Card("7", "Diamonds"),
            Card("7", "Hearts"),
            Card("7", "Clubs"),
            Card("Ace", "Spades")
        ]
        
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Four of a Kind"
        )

    def test_figures_out_straight_flush_is_the_best_rank(self):
        cards = [
            Card("3", "Spades"),
            Card("4", "Spades"),
            Card("5", "Spades"),
            Card("6", "Spades"),
            Card("7", "Spades")
        ]
        
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )      

    def test_figures_out_royal_flush_is_the_best_rank(self):
        cards = [
            Card("10", "Spades"),
            Card("Jack", "Spades"),
            Card("Queen", "Spades"),
            Card("King", "Spades"),
            Card("Ace", "Spades")
        ]
        
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )        




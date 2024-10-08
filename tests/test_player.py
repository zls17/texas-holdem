import unittest
from unittest.mock import MagicMock
from poker.hand import Hand
from poker.player import Player
from poker.card import Card

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name = "Ashish", hand = hand)
        self.assertEqual(player.name, "Ashish")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = "Ashish", hand = mock_hand)
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Ashish", hand = mock_hand)
        cards = [
            Card("Ace", "Spades"),
            Card("7", "Hearts")
        ]
        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)
    
    def test_decides_to_continue_or_drop_out_of_game(self):
        player = Player(name = "Ali", hand = Hand())

        self.assertEqual(
            player.wants_to_fold(),
            False
        )
    
    def test_sorts_player_according_to_best_rank(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (0, "Royal Flush", [])
        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (2, "Four of A Kind", [])

        player1 = Player(name = "Saya", hand = mock_hand1)
        player2 = Player(name = "Nagisa", hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )
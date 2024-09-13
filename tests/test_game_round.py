import unittest
from unittest.mock import MagicMock, call

from poker.card import Card
from poker.game_round import GameRound

class GameRoundTest(unittest.TestCase):
    def setUp(self):
        self.first_two_cards = [
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "7", suit = "Diamonds")
        ]

        self.next_two_cards = [
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "9", suit = "Spades")
        ]

        self.flop_cards = [
            Card("4", "Clubs"),
            Card("Jack", "Spades"),
            Card("Queen", "Hearts")
        ]

        self.turn_card = [
            Card("5", "Hearts")
        ]

        self.river_card = [
            Card("6", "Diamonds")
        ]


    def test_stores_deck_and_players(self):
        deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]

        game_round = GameRound(deck = deck, players = players)

        self.assertEqual(
            game_round.deck,
            deck
        )
        self.assertEqual(
            game_round.players,
            players
        )

    def test_game_play_and_shuffle_deck(self):
        mock_deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck = mock_deck, players = players)

        game_round.play()

        mock_deck.shuffle.assert_called_once()

    def test_deals_two_inital_cards_from_deck_to_each_player(self):
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [mock_player1, mock_player2]
        game_round = GameRound(deck = mock_deck, players = players)

        game_round.play()

        mock_deck.remove_cards.assert_has_calls([
            call(2),
            call(2)
        ])
        mock_player1.add_cards.assert_has_calls([call(self.first_two_cards)])
        mock_player2.add_cards.assert_has_calls([call(self.next_two_cards)])

    def test_removes_player_if_not_willing_to_make_bet(self):
        player1 = MagicMock()
        player2 = MagicMock()
        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False
        players = [player1, player2]
        deck = MagicMock()
        game = GameRound(deck = deck, players = players)
        game.play()

        self.assertEqual(
            players,
            [player2]
        )
    
    def test_deals_each_player_3_flop_1_turn_and_1_river_cards(self):
        player1 = MagicMock()
        player2 = MagicMock()
        player1.wants_to_fold.return_value = False
        player2.wants_to_fold.return_value = False
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]
        players = [player1, player2]

        game_round = GameRound(deck = mock_deck, players = players)
        game_round.play()

        mock_deck.remove_cards.assert_has_calls([call(3), call(1), call(1)])

        calls = [
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)
        ]

        for player in players:
            player.add_cards.assert_has_calls(calls)



        
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound

deck = Deck()

cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
player1 = Player(name = "Ashish", hand = hand1)
player2 = Player(name = "Aniket", hand = hand2)

players = [player1, player2]
game_round = GameRound(deck = deck, players = players)
game_round.play()

# from main import deck, cards, hand1, hand2, player1, player2, game_round


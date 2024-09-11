from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound

deck = Deck()

cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand(cards = [])
hand2 = Hand(cards = [])
hand3 = Hand(cards = [Card("Ace", "Clubs"), Card("Ace", "Diamonds")])
player1 = Player(name = "Ashish", hand = hand1)
player2 = Player(name = "Aniket", hand = hand2)
player3 = Player(name = "Sheldon", hand = hand3)
# from main import deck, cards, hand1, hand2, player1, player2
players = [player1, player2, player3]
game_round = GameRound(deck = deck, players = players)

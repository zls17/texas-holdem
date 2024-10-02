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
hand3 = Hand()
hand4 = Hand()
hand5 = Hand()
hand6 = Hand()

player1 = Player(name = "Sheldon", hand = hand1)
player2 = Player(name = "Leonard", hand = hand2)
player3 = Player(name = "Raj", hand = hand3)
player4 = Player(name = "Howard", hand = hand4)
player5 = Player(name = "Penny", hand = hand5)
player6 = Player(name = "Will", hand = hand6)


players = [player1, player2, player3, player4, player5, player6]

game_round = GameRound(deck = deck, players = players)
game_round.play()

for player in players:
    print(f"{player.name} receives {player.unique_cards}")
    index, best_hand_name, valid_cards = player.best_hand()
    valid_cards = [str(card) for card in valid_cards]
    valid_cards = " and ".join(valid_cards)
    print(f"{player.name} has a {best_hand_name} with cards {valid_cards}")
    print()
    
print(f"The winner is {max(players).name}")
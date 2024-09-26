from poker.validators import RoyalFlushValidator
from poker.validators import StraightFlushValidator
from poker.validators import FourOfAKindValidator
from poker.validators import FullHouseValidator
from poker.validators import FlushValidator
from poker.validators import StraightValidator
from poker.validators import ThreeOfAKindValidator
from poker.validators import TwoPairValidator
from poker.validators import HighCardValidator
from poker.validators import NoCardsValidator
from poker.validators import PairValidator

class Hand():
    def __init__(self):
        self.cards = []
    
    def __repr__(self):
        string_of_cards = [str(card) for card in self.cards]
        return ", ".join(string_of_cards)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    @property
    def _rank_validations_from_best_to_worst(self):
        return (
            ("Royal Flush", RoyalFlushValidator(cards = self.cards).is_valid),
            ("Straight Flush", StraightFlushValidator(cards = self.cards).is_valid),
            ("Four of a Kind", FourOfAKindValidator(cards = self.cards).is_valid),
            ("Full House", FullHouseValidator(cards = self.cards).is_valid),
            ("Flush", FlushValidator(cards = self.cards).is_valid),
            ("Straight", StraightValidator(cards = self.cards).is_valid),
            ("Three of a Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
            ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
            ("Pair", PairValidator(cards = self.cards).is_valid),
            ("High Card", HighCardValidator(cards = self.cards).is_valid),
            ("No Cards", NoCardsValidator(cards = self.cards).is_valid)
        )
    
    def best_rank(self):
        for rank in self._rank_validations_from_best_to_worst:
            rank_name, validator_func = rank
            if validator_func():
                return rank_name
    
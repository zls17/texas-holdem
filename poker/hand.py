from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    HighCardValidator,
    NoCardsValidator,
    PairValidator
)

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
    
    VALIDATOR = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        HighCardValidator,
        NoCardsValidator,
        PairValidator
    )     
    def best_rank(self):
        for index, validator_klass in enumerate(self.VALIDATOR):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())
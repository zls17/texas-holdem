from poker.validators import StraightFlushValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Royal Flush"
    
    def is_valid(self):
        straight_flush = StraightFlushValidator(cards = self.cards)
        if straight_flush.is_valid():
            straight_flush_cards = straight_flush.valid_cards()
            is_royal = straight_flush_cards[-1].rank == "Ace"
            return is_royal

        return False

    def valid_cards(self):
        return StraightFlushValidator(cards = self.cards).valid_cards()
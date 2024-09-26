from poker.validators import FiveCardsInARowValidator

class StraightFlushValidator(FiveCardsInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"
    
    def is_valid(self):
        for five_card in self._collections_of_five_straight_cards_in_a_row:
            unique_suit = {card.suit for card in five_card}
            if (len(unique_suit) == 1):
                return True
        return False

    def valid_cards(self):
        return self._returns_straight_flush_batch[-1]

    @property
    def _returns_straight_flush_batch(self):
        return [
            five_card
            for five_card in self._collections_of_five_straight_cards_in_a_row
            if (len({card.suit for card in five_card})) == 1
        ]
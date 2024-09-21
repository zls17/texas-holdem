from poker.validators import ThreeOfAKindValidator, PairValidator

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()

    def valid_cards(self):
        three_cards = ThreeOfAKindValidator(cards = self.cards).valid_cards()
        two_cards = PairValidator(cards = self.cards).valid_cards()
        cards = three_cards + two_cards
        cards.sort()
        return cards
class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand 
        self.unique_cards = []
        self.community_cards = []

    def __gt__(self, other):
        first_player_best_validator_index = self.best_hand()[0]
        second_player_best_validator_index = other.best_hand()[0]
        return first_player_best_validator_index < second_player_best_validator_index
        
    def best_hand(self):
        return self.hand.best_rank()
    
    def add_cards(self, cards):
        self.hand.add_cards(cards)
    
    def wants_to_fold(self):
        return False


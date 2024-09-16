class StraightValidator():
    def __init__(self, cards):
        self.cards = cards
    
    def is_valid(self):
        if len(self.cards) < 5:
            return False

        return len(self._collections_of_five_straight_cards_in_a_row) >= 1
        
    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_a_row[-1]
    
    @property
    def _collections_of_five_straight_cards_in_a_row(self):
        index = 0
        last_index = len(self.cards) - 1
        collection_of_five_cards_in_a_row = []

        while (index + 4 <= last_index):
            next_five_cards = self.cards[index: index + 5]
            next_five_indices = [card.rank_index for card in next_five_cards]

            if self._every_element_increasing_by_1(next_five_indices):
                collection_of_five_cards_in_a_row.append(next_five_cards)

            index += 1
        
        return collection_of_five_cards_in_a_row

    def _every_element_increasing_by_1(self, rank_indexes):
        first_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(
            range(first_rank_index, last_rank_index + 1))
        return rank_indexes == straight_consecutive_indexes 
 
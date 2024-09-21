class StraightFlushValidator():
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
        pass


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
 
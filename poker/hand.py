class Hand():
    def __init__(self, cards):
        copy = cards[:]
        copy.sort()
        self.cards = copy
    
    @property
    def _rank_validations_from_best_to_worst(self):
        return (
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind", self._four_of_a_kind),
            ("Full House", self._full_house),
            ("Flush", self._flush),
            ("Straight", self._straight),
            ("Three of a Kind", self._three_of_a_kind),
            ("Two Pair", self._two_pair),
            ("Pair", self._pair),
            ("High Card", self._high_card)
        )
    
    def best_rank(self):

        for rank in self._rank_validations_from_best_to_worst:
            rank_name, validator_func = rank
            if validator_func():
                return rank_name
    
    def _royal_flush(self):
        is_straight_flush = self._straight_flush()
        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal

    def _straight_flush(self):
        return self._straight() and self._flush()

    def _four_of_a_kind(self):
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1

    def _full_house(self):
        return self._three_of_a_kind() and self._pair()

    def _flush(self):
        suit_with_count_greater_than_or_equal_to_five = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }
        return len(suit_with_count_greater_than_or_equal_to_five) == 1

    def _straight(self):
        if len(self.cards) < 5:
            return False

        rank_indexes = [card.rank_index for card in self.cards]
        first_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(
            range(first_rank_index, last_rank_index + 1))
        return rank_indexes == straight_consecutive_indexes 
    
    def _three_of_a_kind(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1
            
    def _two_pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2
    
    def _pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1
    
    def _high_card(self):
        return True
    
    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }
        
    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            if card.suit not in card_suit_counts:
                card_suit_counts[card.suit] = 0
            card_suit_counts[card.suit] += 1
        return card_suit_counts

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            if card.rank not in card_rank_counts:
                card_rank_counts[card.rank] = 0
            card_rank_counts[card.rank] += 1
        return card_rank_counts


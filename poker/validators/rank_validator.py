class RankValidator():
    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }
    
    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            if card.rank not in card_rank_counts:
                card_rank_counts[card.rank] = 0
            card_rank_counts[card.rank] += 1
        return card_rank_counts
      
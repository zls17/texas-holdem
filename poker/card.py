class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")

    RANKS = (
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"
            )

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid Rank. Rank must be one of the following: {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid Suit. Suit must be on of the following: {self.SUITS}")
        self.rank = rank
        self.rank_index = self.RANKS.index(self.rank)
        self.suit = suit

    @classmethod
    def create_standard_52_cards(cls):
        return [
            cls(rank, suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank_index < other.rank_index

            
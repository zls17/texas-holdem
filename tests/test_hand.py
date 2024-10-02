import unittest
from poker.card import Card
from poker.hand import Hand 
from poker.validators import PairValidator

class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(
            hand.cards,
            []
        )
    
    def test_shows_all_its_card_in_technical_representation(self):
        cards = [
            Card("Ace", "Spades"),
            Card("Jack", "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            repr(hand),
            "Jack of Clubs, Ace of Spades"
        )

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card("Ace", "Spades")
        seven_of_diamonds = Card("7", "Diamonds")
        cards = [ace_of_spades, seven_of_diamonds]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [seven_of_diamonds, ace_of_spades]
        )


    def test_interacts_with_validator_to_get_winning_hand(self):
        class HandWithOneValidator(Hand):
            VALIDATOR = (PairValidator, )
        
        ace_of_hearts = Card("Ace", "Hearts")
        ace_of_spades = Card("Ace", "Spades")
        cards = [ace_of_hearts, ace_of_spades]

        validator = HandWithOneValidator()

        validator.add_cards(cards = cards)

        self.assertEqual(
            validator.best_rank(),
            (0, "Pair", [ace_of_hearts, ace_of_spades])
        )



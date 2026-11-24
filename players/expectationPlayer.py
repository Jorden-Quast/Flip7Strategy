from .playerBase import PlayerBase
from structure import Deck
from structure.cards import NumberCard

class ExpectationPlayer(PlayerBase):
    """
    Player who's strategy is to only draw if the statistical expectation says they will benefit

    Second order math player, using all information available.
        E(draw) = (1 - P(bust)) * (Current_Score + E(valid cards))
        Where E(x) is the expectation value of the random variables
        Draw if E(draw) > current score (Includes Modifiers)
    """
    ID = "EXPECTATION"

    def __init__(self):
        super().__init__()
        
    def should_draw(self, deck: Deck, other_hands: list[list[int]]) -> bool:
        # If probability indicates that you can expect a better score, hit
        current_score = self.get_hand_score()
        cards_remaining_in_deck = sum(deck.card_counts.values())
        if cards_remaining_in_deck == 0:
            raise ValueError("Cannot Take Turn, No Cards Remaining")

        # Get Bust Probability
        bust_cards = 0
        for card in self.hand:
            bust_cards += deck.card_counts[card]
        bust_probability = bust_cards / cards_remaining_in_deck

        # Get expected value of next card
        available_cards = cards_remaining_in_deck - bust_cards
        if available_cards == 0: # If literally nothing can be drawn, we definitely shouldn't take turn
            return False

        expected_next_card = 0
        for card, count in deck.card_counts.items():
            if card in self.hand:
                continue
            if not isinstance(card, NumberCard):
                continue

            expected_next_card += (count / available_cards) * card.point_value

        # Check for bonus
        seven_card_bonus = 0
        if len(self.hand) == 6:
            seven_card_bonus = 15

        expected_hit_score = (1 - bust_probability) * (current_score + expected_next_card + seven_card_bonus)
        return current_score < expected_hit_score
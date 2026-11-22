from .playerBase import PlayerBase
from structure import Deck

class ProbabilityPlayer(PlayerBase):
    ID = "PROBABILITY"
    
    def __init__(self, probability_threshold: float, probability_error: float = 0):
        super().__init__()

        if probability_threshold < 0 or probability_threshold > 1:
            raise ValueError("Probability Threshold must be between 0 and 1")
        if probability_error < -1 or probability_error > 1:
            raise ValueError("Probability Error must be between -1 and 1")


        self.probability_threshold = probability_threshold
        self.probability_error = probability_error

    def should_draw(self, deck: Deck, other_hands: list[list[int]]) -> bool:
        # If the probability of busting is below a (estimated) threshold, hit
        bust_cards = 0
        for card in self.hand:
            bust_cards += deck.card_counts.get(card, 0)

        raw_bust_probability = bust_cards / sum(deck.card_counts.values())
        used_probability = max(min((raw_bust_probability + self.probability_error), 1), 0)

        return used_probability < self.probability_threshold
from players.playerState import PlayerState
from strategies import Strategy
from structure.deck import Deck

class RiskTolerance(Strategy):
    """
    A player who's strategy is to draw only if the bust probability is below a certain level

    The first-order math player, draws only if P(bust) < probability threshold
    """

    STRATEGY_NAME = "Risk Tolerance"

    def __init__(self, probability_threshold: float):
        super().__init__()

        if probability_threshold < 0 or probability_threshold > 1:
            raise ValueError("Probability Threshold must be between 0 and 1")

        self.probability_threshold = probability_threshold

    def should_draw(self, player_state: PlayerState, deck: Deck) -> bool:
        bust_cards = 0
        for card in player_state.hand:
            bust_cards += deck.card_counts.get(card, 0)

        bust_probability = bust_cards / sum(deck.card_counts.values())
        return bust_probability < self.probability_threshold

from strategies import Strategy
from players import PlayerState
from structure.deck import Deck

class ScoreGoal(Strategy):
    """
    A player who's strategy is to reach a certain score, optionally including modifiers

    Only draws if current score < score threshold
    """

    STRATEGY_NAME = "Score Goal"

    def __init__(self, score_threshold: int, include_modifiers: bool):
        super().__init__()

        if score_threshold < 1 or score_threshold > 63:
            raise ValueError("Score Threshold Must Be Between 1 and 63 (Does not Account For Modifiers)")

        self.score_threshold = score_threshold
        self.include_modifiers = include_modifiers

    def should_draw(self, player_state: PlayerState, deck: Deck) -> bool:
        # Score Player: Once we've reached a certain score we stop
        return player_state.get_score(self.include_modifiers) < self.score_threshold

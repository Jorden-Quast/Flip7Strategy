from .playerBase import PlayerBase
from structure import Deck

class ScorePlayer(PlayerBase):
    """
    A player who's strategy is to reach a certain raw hand score.

    Does not account for modifier cards, just whether the 7 countable cards
    reach an acceptable score, drawing if current score < score threshold
    """
    ID = "SCORE"
    def __init__(self, score_threshold: int):
        super().__init__()

        if score_threshold < 1 or score_threshold > 63:
            raise ValueError("Score Threshold Must Be Between 1 and 63 (Does not Account For Modifiers)")

        self.score_threshold = score_threshold

    def should_draw(self, deck: Deck, other_hands: list[list[int]]) -> bool:
        # Score Player: Once we've reached a certain score we stop
        return self.get_hand_score() < self.score_threshold
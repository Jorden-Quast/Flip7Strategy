from .playerBase import PlayerBase
from structure import Deck

class ScorePlayer(PlayerBase):
    ID = "SCORE"
    def __init__(self, score_threshold: int):
        super().__init__()

        self.score_threshold = score_threshold

    def should_draw(self, deck: Deck, other_hands: list[list[int]]) -> bool:
        # Score Player: Once we've reached a certain score we stop
        return self.get_hand_score() < self.score_threshold
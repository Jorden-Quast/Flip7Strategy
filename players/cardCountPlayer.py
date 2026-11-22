from .playerBase import PlayerBase
from structure import Deck

class CardCountPlayer(PlayerBase):
    ID = "COUNT"
    def __init__(self, card_threshold: int):
        super().__init__()

        if card_threshold < 0 or card_threshold > 7:
            raise ValueError("Unreachable number of cards given")
        self.card_threshold = card_threshold

    def should_draw(self, deck: Deck, other_hands: list[list[int]]):
        # Card Count Player: If we have a certain number of cards we stop
        return len(self.hand) < self.card_threshold
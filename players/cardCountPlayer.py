from .playerBase import PlayerBase
from structure import Deck

class CardCountPlayer(PlayerBase):
    """
    A player who's strategy is simply to reach a set number of cards.

    They come into the game with some card threshold in mind, and will only
    draw if the number of cards in their hand is less than that threshold
    """
    ID = "COUNT"
    def __init__(self, card_threshold: int):
        super().__init__()

        if card_threshold < 1 or card_threshold > 7:
            raise ValueError("Unreachable number of cards given")
        self.card_threshold = card_threshold

    def should_draw(self, deck: Deck, other_hands: list[list[int]]):
        # Card Count Player: If we have a certain number of cards we stop
        return len(self.hand) < self.card_threshold
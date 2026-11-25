from strategies import Strategy
from structure import PlayerState, Deck

class CardCount(Strategy):
    """
    The strategy of just reaching a set number of cards.

    Defines some threshold, and only allows draw if the number of cards in hand
    is less than that of the threshold
    """
    STRATEGY_NAME = "Card Count"

    def __init__(self, card_threshold: int):
        super().__init__()

        if card_threshold < 1 or card_threshold > 7:
            raise ValueError("Unreachable number of cards given")
        self.card_threshold = card_threshold

    def should_draw(self, player_state: PlayerState, deck: Deck):
        return len(player_state.hand) < self.card_threshold
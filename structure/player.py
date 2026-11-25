from __future__ import annotations
from typing import TYPE_CHECKING
from .playerState import PlayerState
from structure.cards import NumberCard, ModifierCard

if TYPE_CHECKING:
    from strategies import Strategy
    from structure import Deck


class Player:
    """
    Class representing an arbitrary "Player"

    Has the shared logic for how players behave inside a game and
    round, but leaves logic or planning decisions up to the provided
    strategy and personality
    """
    def __init__(self, strategy: Strategy):
        # Personal info
        self.strategy = strategy
        
        # Score and Game Data
        self.total_score = 0
        self.rounds_to_win = -1
        self.round_state: PlayerState = PlayerState()

    def take_turn(self, deck: Deck) -> None:
        # If already staying or have busted, can't change
        if self.round_state.stay or self.round_state.bust:
            return

        # If we have cards, check if we should continue
        if (len(self.round_state.hand) > 0): 
            # Check if we're continuing on or deciding to stay
            should_draw = self.strategy.should_draw(self.round_state, deck)
            if not should_draw:
                self.round_state.stay = True
                return

        # Otherwise, pull and resolve a card
        card = deck.draw_card()
        if card in self.round_state.hand:
            self.round_state.bust = True

        if isinstance(card, NumberCard):
            self.round_state.hand.append(card)
        elif isinstance(card, ModifierCard):
            self.round_state.modifiers.append(card)

    def end_round(self) -> None:
        # Add total score if possible
        if not self.round_state.bust:
            self.total_score += self.round_state.get_score(True)

            # Give 15 pt bonus for reaching 7 cards
            if len(self.round_state.hand) == 7:
                self.total_score += 15

        # Reset turn variables
        self.round_state = PlayerState()
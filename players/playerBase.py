from abc import ABC, abstractmethod
from structure import Deck
from structure.cards import *

class PlayerBase(ABC):
    ID = "BASE"

    def __init__(self):
        # Player Status
        self.stay: bool = False
        self.bust: bool = False
        self.hand: list[NumberCard] = []

        # Score and Game Data
        self.total_score = 0
        self.rounds_to_win = -1

    def take_turn(self, deck: Deck, other_hands: list[list[int]]) -> None:
        # If already staying or have busted, can't change
        if self.stay or self.bust:
            return

        # If we have cards, and we don't have the zero, check if we should continue
        if (len(self.hand) > 0) and not any(isinstance(c, Zero) for c in self.hand): 
            # Check if we're continuing on or deciding to stay
            should_draw = self.should_draw(deck, other_hands)
            if not should_draw:
                self.stay = True
                return

        # Otherwise, pull and resolve a card
        card = deck.draw_card()
        if card in self.hand:
            self.bust = True

        if isinstance(card, NumberCard):
            self.hand.append(card)


    def end_round(self) -> None:
        # Add total score if possible
        if not self.bust:
            self.total_score += sum(card.point_value for card in self.hand)

            # Give 15 pt bonus for reaching 7 cards
            if len(self.hand) == 7:
                self.total_score += 15

        # Reset turn variables
        self.stay = False
        self.bust = False
        self.hand = []

    def get_hand_score(self) -> int:
        return sum(card.point_value for card in self.hand)

    @abstractmethod
    def should_draw(self, deck: Deck, other_hands: list[list[int]]) -> bool:
        pass
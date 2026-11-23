from structure.cards import *
from random import randint

class Deck:
    def __init__(self):
        self.card_counts: dict[Card, int] = {}
        for i in range(1, 12):
            self.card_counts[Number(i)] = i
        
        # Add Special Number Cards
        self.card_counts[Zero()] = 1

    def draw_card(self) -> Card:
        # Get the total number of cards remaining
        num_opts = sum(self.card_counts.values())
        if num_opts == 0:
            raise ValueError("No Valid Options Remaining")

        # Select a random one from the stack by index, then search for it
        selected_idx = randint(0, num_opts - 1)
        drawn_card = -1
        for card, count in self.card_counts.items():
            selected_idx -= count
            if selected_idx < 0:
                drawn_card = card
                break

        if drawn_card == -1:
            raise ValueError(f"Failed to draw a card")

        # Decrease count to show it's been taken and return it
        self.card_counts[drawn_card] -= 1
        return drawn_card


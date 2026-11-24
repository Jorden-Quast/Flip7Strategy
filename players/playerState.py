from dataclasses import dataclass, field
from structure.cards import NumberCard, ModifierCard, ModifierMult, ModifierSum

@dataclass()
class PlayerState:
    """Represents the state of a player inside a round"""
    stay: bool = False
    bust: bool = False
    hand: list[NumberCard] = field(default_factory=list[NumberCard])
    modifiers: list[ModifierCard] = field(default_factory=list[ModifierCard])

    def get_score(self, include_modifiers: bool) -> int:
        """
        Gets the current score of the player for a round

        Parameters
        ----------
        include_modifiers: bool
            Wether to consider any modifier cards when calculating score
        
        Returns
        -------
        int
            The players current score
        """

        score = sum(card.point_value for card in self.hand)
        if not include_modifiers or not self.modifiers:
            return score

        multiplier = 1
        for card in self.modifiers:
            if isinstance(card, ModifierSum):
                score += card.point_value
            elif isinstance(card, ModifierMult):
                multiplier = card.multiplier
            else:
                raise ValueError("How did we get here?")
        
        return multiplier * score

from dataclasses import dataclass, field
from structure.cards import NumberCard, ModifierCard, ModifierSum

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

        By the rules, modifier cards first add bonus points
        *then* multiply

        Parameters
        ----------
        include_modifiers: bool
            Wether to consider any modifier cards when calculating score
        
        Returns
        -------
        int
            The players current score
        """

        hand_score = sum(card.point_value for card in self.hand)
        if not include_modifiers or not self.modifiers:
            return hand_score

        multiplier = 1
        extra_points = 0
        for card in self.modifiers:
            if isinstance(card, ModifierSum):
                extra_points += card.point_value
            else:
                multiplier = card.multiplier
        
        return (multiplier * hand_score) + extra_points

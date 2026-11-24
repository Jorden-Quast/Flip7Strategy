from dataclasses import dataclass, field
from structure.cards import NumberCard, ModifierCard

@dataclass()
class PlayerState:
    """Represents the state of a player inside a round"""
    stay: bool = False
    bust: bool = False
    hand: list[NumberCard] = field(default_factory=list[NumberCard])
    modifiers: list[ModifierCard] = field(default_factory=list[ModifierCard])

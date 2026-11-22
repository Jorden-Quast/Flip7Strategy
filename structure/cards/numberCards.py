from abc import ABC
from dataclasses import dataclass

@dataclass(frozen=True)
class NumberCard(ABC):
    point_value: int

@dataclass(frozen=True)
class Number(NumberCard):
    """Standard Number Card with some point value"""
    pass

@dataclass(frozen=True)
class Zero(NumberCard):
    """Zero Number Card: No points, forces receiving player to go for flip 7"""
    point_value: int = 0

@dataclass(frozen=True)
class UnluckySeven(NumberCard):
    """Unlucky Seven: Receiving player discards everything but this card"""
    point_value: int = 7

@dataclass(frozen=True)
class LuckyThirteen(NumberCard):
    """Lucky Thirteen: Receiving player can have a second thirteen in their hand"""
    point_value: int = 13
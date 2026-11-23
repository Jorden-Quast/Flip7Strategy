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
    """Zero Number Card: No points, but counts towards flip 7 goal"""
    point_value: int = 0

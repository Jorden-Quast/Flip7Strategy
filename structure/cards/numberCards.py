from abc import ABC
from dataclasses import dataclass

@dataclass(frozen=True)
class NumberCard(ABC):
    point_value: int

    def __post_init__(self):
        if self.point_value < 0 or self.point_value > 12:
            raise ValueError("Number Cards Must Be Between 0 and 12")

@dataclass(frozen=True)
class Number(NumberCard):
    """Standard Number Card with some point value"""

    def __post_init__(self):
        super().__post_init__()
        if self.point_value == 0:
            raise ValueError("Number should be between 1 and 12, use the Zero class for 0")

@dataclass(frozen=True)
class Zero(NumberCard):
    """Zero Number Card: No points, but counts towards flip 7 goal"""
    point_value: int = 0

    def __post_init__(self):
        super().__post_init__()

        if self.point_value != 0:
            raise ValueError("Value should only be zero")

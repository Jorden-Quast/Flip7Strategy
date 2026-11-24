from dataclasses import dataclass

@dataclass(frozen=True)
class ModifierSum:
    """Modifier cards which adds some amount to score"""
    point_value: int

    def __post_init__(self):
        if self.point_value < 2 or self.point_value > 10:
            raise ValueError("All modifiers should be even numbers between 2 and 10 points")
        if self.point_value % 2 != 0:
            raise ValueError("All modifiers should be even numbers between 2 and 10 points")

@dataclass(frozen=True)
class ModifierMult:
    """x2 Modifier card which doubles the players total score"""
    multiplier: int = 2

    def __post_init__(self):
        if self.multiplier != 2:
            raise ValueError("Multiplier should only be 2")

ModifierCard = ModifierSum | ModifierMult

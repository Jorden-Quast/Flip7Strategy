from dataclasses import dataclass

@dataclass(frozen=True)
class ModifierSum:
    """Modifier cards which subtracts some amount from score"""
    point_value: int

@dataclass(frozen=True)
class ModifierMult:
    """(1/2) Modifier card which divides the players total score"""
    multiplier: float = 0.5

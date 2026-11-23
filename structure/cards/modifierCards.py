from dataclasses import dataclass

@dataclass(frozen=True)
class ModifierSum:
    """Modifier cards which adds some amount to score"""
    point_value: int

@dataclass(frozen=True)
class ModifierMult:
    """x2 Modifier card which doubles the players total score"""
    multiplier: int = 2

ModifierCard = ModifierSum | ModifierMult

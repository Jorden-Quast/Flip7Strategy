from dataclasses import dataclass

@dataclass(frozen=True)
class ActionSecondChance:
    """Second Chance: Allows the player to draw a duplicate card without busting"""
    pass

@dataclass(frozen=True)
class ActionFreeze:
    """Freeze Action Card: Forces target player to stay"""
    pass

@dataclass(frozen=True)
class ActionFlipThree:
    """
    Flip Three Action Card: Forces target player to accept the next three cards
    Busting or Reaching 7 Cards interrupts process 
    """
    pass

ActionCard = ActionSecondChance | ActionFlipThree | ActionFreeze
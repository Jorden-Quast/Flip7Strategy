from dataclasses import dataclass

@dataclass(frozen=True)
class ActionSecondChance:
    """
    Second Chance: Allows the player to draw a duplicate card without busting
    If receiving player already has a second chance card, they must the new one to someone else
    If all players already have a second chance card, do nothing
    """
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
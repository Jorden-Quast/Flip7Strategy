from dataclasses import dataclass

@dataclass(frozen=True)
class ActionJustOneMore:
    """Just One More Action Card: Forces target player to accept one card then stay"""
    pass

@dataclass(frozen=True)
class ActionSwap:
    """Swap Action Card: Swaps *any* two cards currently in play"""
    pass

@dataclass(frozen=True)
class ActionSteal:
    """Steal Action Card: Steals any card from another player"""
    pass

@dataclass(frozen=True)
class ActionDiscard:
    """Discard Action Card: Discard any card currently in play"""
    pass

@dataclass(frozen=True)
class ActionFlipFour:
    pass
from structure.cards.actionCards import *
from structure.cards.modifierCards import *
from structure.cards.numberCards import *

ModifierCard = ModifierSum | ModifierMult
ActionCard = ActionJustOneMore | ActionSwap | ActionSteal | ActionDiscard | ActionFlipFour
Card = NumberCard | ModifierCard | ActionCard

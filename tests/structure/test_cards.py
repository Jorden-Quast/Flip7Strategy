import pytest
from structure.cards import *

def test_number_valid():
    """ Tests that the number cards can be created"""
    Number(5)
    Zero()

def test_number_invalid_low():
    """ Tests that number cards reject points < 1"""
    with pytest.raises(ValueError):
        Number(0)

def test_number_invalid_high():
    """ Tests that number cards reject points > 12"""
    with pytest.raises(ValueError):
        Number(13)

def test_change_zero_raises_error():
    """ Tests that the Zero card cannot be set otherwise """
    with pytest.raises(ValueError):
        Zero(5)

def test_actions():
    """ Tests that action cards can be created """
    ActionFreeze()
    ActionFlipThree()

def test_modifiers_valid():
    """ Tests that modifier cards can be created with good values """
    ModifierSum(4)
    ModifierMult()

def test_modifier_sum_invalid_low():
    """ Tests that modifier sum cards reject values < 2"""
    with pytest.raises(ValueError):
        ModifierSum(0)

def test_modifier_sum_invalid_high():
    """ Tests that modifier sum cards reject values > 10"""
    with pytest.raises(ValueError):
        ModifierSum(12)

def test_modifier_sum_invalid_odd():
    """ Tests that modifier sum cards reject odd values"""
    with pytest.raises(ValueError):
        ModifierSum(5)

def test_change_modifier_mult_raises_error():
    """ Tests that the multiplier modifier cannot be changed from 2"""
    with pytest.raises(ValueError):
        ModifierMult(3)


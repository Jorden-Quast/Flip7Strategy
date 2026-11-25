import pytest
from strategies import CardCount
from structure import PlayerState
from structure import Deck
from structure.cards import NumberCard

def test_valid_card_threshold_bottom():
    """ Checks that the minimum valid card threshold is accepted and stored """
    card_threshold = 1
    strategy = CardCount(card_threshold)  # Should not throw an error
    assert strategy.card_threshold == card_threshold

def test_valid_card_threshold_mid():
    """ Checks that a middle valid card threshold is accepted and stored """
    card_threshold = 4
    strategy = CardCount(card_threshold)  # Should not throw an error
    assert strategy.card_threshold == card_threshold

def test_valid_card_threshold_top():
    """ Checks that the maximum valid card threshold is accepted and stored """
    card_threshold = 7
    strategy = CardCount(card_threshold)  # Should not throw an error
    assert strategy.card_threshold == card_threshold

def test_invalid_card_threshold_low():
    """ Checks that a card threshold < 1 is not accepted """
    with pytest.raises(ValueError):
        CardCount(0)

def test_invalid_card_threshold_high():
    """ Checks that a card threshold > 7 is not accepted """
    with pytest.raises(ValueError):
        CardCount(8)

def test_should_draw_positive():
    """ Checks that the player draws a card when the current number of cards in their hand < the threshold """
    strategy = CardCount(3)
    assert strategy.should_draw(PlayerState(), Deck()) 

def test_should_draw_negative():
    """ Checks that the player does not draw a card when the current number of cards in their hand >= the threshold
    """
    strategy = CardCount(1)
    player_state = PlayerState(hand=[NumberCard(0)])
    assert not strategy.should_draw(player_state, Deck())

def test_name_set():
    """ Checks that the id is set"""
    assert CardCount.STRATEGY_NAME != ""
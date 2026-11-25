import pytest # type: ignore
from structure import PlayerState
from strategies import MaximumExpectation
from structure import Deck 
from structure.cards import NumberCard

def test_can_create():
    """ Test that the object can be created without exceptions"""
    MaximumExpectation()  

def test_can_draw_positive():
    """ Test that the player will draw a card if E(draw) > current score"""
    # Create Player and set their hand
    strategy = MaximumExpectation()
    player_state = PlayerState(hand=[NumberCard(2)])

    # Create a custom deck
    deck = Deck()
    deck.card_counts = {
        NumberCard(2) : 1,
        NumberCard(11) : 11,
        NumberCard(12) : 12,
    }

    """
    Given this player and deck:
        P(bust) = 1 / 24 = 0.04166
        E(valid) = 11 * (11/23) + 12 * (12/23) = 16.3377
    So, E(draw) = (1 - P(bust)) * (2 + E(valid)) = 17.5737
    Since this is greater than 1, the player should draw
    """
    assert strategy.should_draw(player_state, deck)

def test_can_draw_negative():
    """ Test that the player will not draw the card if E(draw) <= current score"""
    # Create Player and set their hand
    strategy = MaximumExpectation()
    player_state = PlayerState(hand=[NumberCard(4)])

    # Create a custom deck
    deck = Deck()
    deck.card_counts = {
        NumberCard(0) : 1,
        NumberCard(4) : 2,
        NumberCard(8) : 1
    }

    """
    Given this player and deck:
        P(bust) = 2 / 4 = 0.5
        E(valid) = 0 * (1/2) + 8 * (1/2) = 4
    So E(draw) = (1 - P(B)) * (4 + E(valid)) = 4 
    Since this is not strictly less than the players current hand, the player should not draw
    """
    assert not strategy.should_draw(player_state, deck)
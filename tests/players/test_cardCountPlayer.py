import pytest # type: ignore
from players.cardCountPlayer import CardCountPlayer
from structure.deck import Deck
from structure.cards import NumberCard

def test_valid_card_threshold_bottom():
    """ Checks that the minimum valid card threshold is accepted and stored """
    card_threshold = 1
    player = CardCountPlayer(card_threshold)  # Should not throw an error
    assert player.card_threshold == card_threshold

def test_valid_card_threshold_mid():
    """ Checks that a middle valid card threshold is accepted and stored """
    card_threshold = 4
    player = CardCountPlayer(card_threshold)  # Should not throw an error
    assert player.card_threshold == card_threshold

def test_valid_card_threshold_top():
    """ Checks that the maximum valid card threshold is accepted and stored """
    card_threshold = 7
    player = CardCountPlayer(card_threshold)  # Should not throw an error
    assert player.card_threshold == card_threshold

def test_invalid_card_threshold_low():
    """ Checks that a card threshold < 1 is not accepted """
    with pytest.raises(ValueError):
        CardCountPlayer(0)

def test_invalid_card_threshold_high():
    """ Checks that a card threshold > 7 is not accepted """
    with pytest.raises(ValueError):
        CardCountPlayer(8)

def test_should_draw_positive():
    """ Checks that the player draws a card when the current number of cards in their hand < the threshold """
    player = CardCountPlayer(3)
    assert player.should_draw(Deck(), [])

def test_should_draw_negative():
    """ Checks that the player does not draw a card when the current number of cards in their hand >= the threshold """
    player = CardCountPlayer(1)
    player.hand.append(NumberCard(0))
    assert not player.should_draw(Deck(), [])

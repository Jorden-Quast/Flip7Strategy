import pytest
from structure import PlayerState
from strategies import ScoreGoal
from structure import Deck
from structure.cards import NumberCard

# TODO: Implement tests for modifiers

def test_valid_score_threshold_bottom():
    """ Checks that the minimum valid score threshold is accepted and stored """
    score_threshold = 1
    strategy = ScoreGoal(score_threshold, False)
    assert strategy.score_threshold == score_threshold

def test_valid_score_threshold_mid():
    """ Checks that a middle valid score threshold is accepted and stored """
    score_threshold = 30
    strategy = ScoreGoal(score_threshold, False)
    assert strategy.score_threshold == score_threshold

def test_valid_score_threshold_top():
    """ Checks that the maximum valid score threshold is accepted and stored """
    score_threshold = 63
    strategy = ScoreGoal(score_threshold, False)
    assert strategy.score_threshold == score_threshold

def test_invalid_score_threshold_low():
    """ Checks that a score threshold < 1 is not accepted """
    with pytest.raises(ValueError):
        ScoreGoal(0, False)

def test_invalid_score_threshold_high():
    """ Checks that a score threshold > 63 is not accepted. 63 = sum(6 through 12) """

    with pytest.raises(ValueError):
        ScoreGoal(64, False)

def test_should_draw_positive():
    """ Checks that the player draws a card when their score < the threshold """
    strategy = ScoreGoal(25, False)
    assert strategy.should_draw(PlayerState(), Deck())

def test_should_draw_negative():
    """ Checks that the player does not draw a card when their score >= the threshold """
    strategy = ScoreGoal(7, False)
    player_state = PlayerState(hand=[NumberCard(12)])
    assert not strategy.should_draw(player_state, Deck())
import pytest # type: ignore
from players import ScorePlayer
from structure import Deck
from structure.cards import NumberCard

def test_valid_score_threshold_bottom():
    """ Checks that the minimum valid card threshold is accepted and stored """
    score_threshold = 1
    player = ScorePlayer(score_threshold)
    assert player.score_threshold == score_threshold

def test_valid_score_threshold_mid():
    """ Checks that a middle valid card threshold is accepted and stored """
    score_threshold = 30
    player = ScorePlayer(score_threshold)
    assert player.score_threshold == score_threshold

def test_valid_score_threshold_top():
    """ Checks that the maximum valid card threshold is accepted and stored """
    score_threshold = 63
    player = ScorePlayer(score_threshold)
    assert player.score_threshold == score_threshold

def test_invalid_score_threshold_low():
    """ Checks that a score threshold < 1 is not accepted """
    with pytest.raises(ValueError):
        ScorePlayer(0)

def test_invalid_score_threshold_high():
    """ Checks that a score threshold > 63 is not accepted. 63 = sum(6 through 12) """
    with pytest.raises(ValueError):
        ScorePlayer(64)

def test_should_draw_positive():
    """ Checks that the player draws a card when their score < the threshold """
    player = ScorePlayer(25)
    assert player.should_draw(Deck(), [])

def test_should_draw_negative():
    """ Checks that the player does not draw a card when their score >= the threshold """
    player = ScorePlayer(7)
    player.hand.append(NumberCard(12))
    assert not player.should_draw(Deck(), [])
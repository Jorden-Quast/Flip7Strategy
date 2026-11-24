import pytest
from players import ProbabilityPlayer
from structure import Deck
from structure.cards import NumberCard

def test_valid_probability_threshold_bottom():
    """ Checks that the minimum valid probability threshold is accepted and stored"""
    probability_threshold = 0
    player = ProbabilityPlayer(probability_threshold)
    assert player.probability_threshold == probability_threshold

def test_valid_probability_threshold_mid():
    """ Checks that a middle valid probability threshold is accepted and stored"""
    probability_threshold = 0.5
    player = ProbabilityPlayer(probability_threshold)
    assert player.probability_threshold == probability_threshold

def test_valid_probability_threshold_top():
    """ Checks that a top valid probability threshold is accepted and stored"""
    probability_threshold = 1
    player = ProbabilityPlayer(probability_threshold)
    assert player.probability_threshold == probability_threshold

def test_invalid_probability_threshold_low():
    """ Checks that a low probability threshold is rejected """
    with pytest.raises(ValueError):
        ProbabilityPlayer(-0.5)

def test_invalid_probability_threshold_high():
    """ Checks that a high probability threshold is rejected """
    with pytest.raises(ValueError):
        ProbabilityPlayer(1.1)

def should_draw_positive():
    """Checks that a player draws a card when the probability of busting is low enough"""
    # Create custom deck
    deck = Deck()
    deck.card_counts = {
        NumberCard(2) : 2,
        NumberCard(4) : 2
    }

    # Create player, add a card to their hand
    player = ProbabilityPlayer(0.75)
    player.hand = [NumberCard(2)]

    # Because the deck has 4 cards: 2 2's and 2 4's, the probability of busting
    # is only 0.5, so a player with a threshold of 0.75 should return true
    assert player.should_draw(deck, [])

def should_draw_negative():
    """Checks that a player does not draw a card when the probability of busting is too high"""
    # Create custom deck
    deck = Deck()
    deck.card_counts = {
        NumberCard(2) : 2,
        NumberCard(4) : 2
    }

    # Create player, add a card to their hand
    player = ProbabilityPlayer(0.5)
    player.hand = [NumberCard(2)]

    # Because the deck has 4 cards: 2 2's and 2 4's, the probability of busting
    # is 0.5, so a player with a threshold of 0.5 should return false because
    # the player is defined to strictly only draw if P(bust) < probability_threshold
    assert not player.should_draw(deck, [])



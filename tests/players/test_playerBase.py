import pytest # type: ignore
from players import CardCountPlayer
from structure import Deck
from structure.cards import NumberCard

def test_empty_hand_draw():
    """If a player has no cards, they should draw on their turn"""
    player = CardCountPlayer(7)
    player.take_turn(Deck(), [])

    assert len(player.hand) == 1

def test_take_turn_choose_to_draw_positive():
    """ If a player can draw, and choose to, they do"""

    # Setup player
    player = CardCountPlayer(7)
    player.hand = [NumberCard(1)]

    # Setup Deck to ensure no busting issues
    deck = Deck()
    deck.card_counts = {
        NumberCard(2) : 2,
        NumberCard(3) : 3
    }
    player.take_turn(deck, [])

    assert len(player.hand) == 2

def test_take_turn_choose_to_stay():
    """ If a player can draw, but choose not to, they don't and the stay flag gets set"""

    # Setup player
    player = CardCountPlayer(1)
    player.hand = [NumberCard(1)]

    # Setup Deck to ensure no busting issues
    deck = Deck()
    deck.card_counts = {
        NumberCard(2) : 2,
        NumberCard(3) : 3
    }
    player.take_turn(deck, [])

    assert len(player.hand) == 1 and player.stay

def test_take_turn_bust_after_draw():
    """ If a player draws a card causing a bust, the flag gets set"""

    # Setup Player
    player = CardCountPlayer(7)
    player.hand = [NumberCard(2)]

    # Setup deck to guarantee a bust
    deck = Deck()
    deck.card_counts = {
        NumberCard(2) : 1
    }
    player.take_turn(deck, [])

    assert player.bust

def test_take_turn_bust_prevents_turn():
    """ If a player is busted, don't take turn"""

    # Setup player
    player = CardCountPlayer(7)
    player.bust = True

    # Setup deck to ensure only number cards are available
    deck = Deck()
    deck.card_counts = {
        NumberCard(0) : 1,
    }

    # If the bust isn't respected, the empty-handed player will draw
    player.take_turn(deck, [])
    assert len(player.hand) == 0

def test_take_turn_stay_prevents_turn():
    """ If a player has chosen to stay, don't take turn"""

    # Setup player
    player = CardCountPlayer(7)
    player.stay = True

    # Setup deck to ensure only number cards are available
    deck = Deck()
    deck.card_counts = {
        NumberCard(0) : 1,
    }

    # If the stay isn't respected, the empty-handed player will draw
    player.take_turn(deck, [])
    assert len(player.hand) == 0

def test_end_round_adds_score_no_bonus():
    """ If a player is in a valid state and less than seven cards, add sum to score """

    # Setup Player
    player = CardCountPlayer(7)
    player.hand = [NumberCard(1), NumberCard(2), NumberCard(3)]

    player.end_round()
    assert player.total_score == 6

def test_end_round_adds_score_with_bonus():
    """ If a player is in a valid state with seven cards, add sum to score plus 15 point bonus"""

    # Setup Player
    player = CardCountPlayer(7)
    player.hand = [NumberCard(1), NumberCard(2), NumberCard(3), NumberCard(4),
                   NumberCard(5), NumberCard(6), NumberCard(7)]

    player.end_round()
    assert player.total_score == (1 + 2 + 3 + 4 + 5 + 6 + 7 + 15)

def test_end_round_no_score_on_bust():
    """ If a player is busted, they should get no points"""

    # Setup Player
    player = CardCountPlayer(7)
    player.bust = True
    player.hand = [NumberCard(1), NumberCard(2), NumberCard(3)]

    player.end_round()
    assert player.total_score == 0

def test_end_round_score_on_stay():
    """ If a player has stayed, they should still score"""

    # Setup Player
    player = CardCountPlayer(7)
    player.stay = True
    player.hand = [NumberCard(1), NumberCard(2), NumberCard(3)]

    player.end_round()
    assert player.total_score == 6

def test_end_round_resets_state():
    """ Ending the round resets all flags and clears hand for next round """

    # Setup Player
    player = CardCountPlayer(7)
    player.bust = True
    player.stay = True
    player.hand = [NumberCard(1), NumberCard(2), NumberCard(3)]

    player.end_round()
    assert not player.bust and not player.stay and not player.hand

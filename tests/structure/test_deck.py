import pytest  # type: ignore
from structure import Deck
from structure.cards import *

def test_deck_contents():
    """
    Checks that the expected number of cards (and their types) are there.

    Should be:

        - 77 Standard Number Cards (12 - 1)
        - 1  Zero Card
        
        TODO:
        - 5  Addition Modifier Cards (2, 4, 6, 8, 10)
        - 1  x2 Modifier Cards (x2)
        - 3  Freeze Cards
        - 3  Flip Three Cards
        - 3  Second Chance Cards
    """
    errors: list[str] = []

    deck = Deck()

    # Check that the total number of cards is correct
    expected_num_cards = 79
    measured_num_cards = sum(deck.card_counts.values())
    if measured_num_cards != expected_num_cards:
        errors.append(f"Incorrect Total Number of Cards. Expecting {expected_num_cards}, got {measured_num_cards}")

    # Check that the count of each individual type is right
    for card, count in deck.card_counts.items():
        if isinstance(card, Number) and card.point_value != count:
            errors.append(f"Incorrect Number of Cards for {card.point_value}. "+
                          f"Expecting {card.point_value}, got {count}")
        if isinstance(card, Zero) and count != 1:
            errors.append(f"Incorrect Number of Cards for Zero. "+
                          f"Expecting {1}, got {count}")

    assert not errors, "Errors Occurred: " + "; ".join(errors)

def test_draw_card_valid():
    """ Tests that calling draw_card returns a value"""

    # Set deck to a known state of a single card to deal with randomness
    deck = Deck()
    deck.card_counts = {NumberCard(4) : 4}

    card = deck.draw_card()
    assert isinstance(card, NumberCard) and deck.card_counts[NumberCard(4)] == 3

def test_draw_card_empty():
    """ Tests that calling draw_card on an empty deck raises an exception """
    # Set deck to be empty
    deck = Deck()
    deck.card_counts = {}

    # Trying to draw from an empty deck should raise an exception
    with pytest.raises(ValueError):
        deck.draw_card()
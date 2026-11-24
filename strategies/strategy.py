from abc import ABC, abstractmethod
from players import PlayerState
from structure import Deck

class Strategy(ABC):
    STRATEGY_NAME = ""

    @abstractmethod
    def should_draw(self, player_state: PlayerState, deck: Deck) -> bool:
        """
        Determine if the player should draw based on the defined strategy and player state

        Parameters
        ----------
        player_state: PlayerState
            The current state of the player deciding wether to draw
        deck: Deck
            The round game deck
        
        Returns
        -------
        bool:
            Flag representing wether the player has decided to draw this turn
        """
        pass
from random import uniform, randint
from structure import Deck, Player
from strategies import *

class Game:
    def __init__(self, num_players: int):
        if num_players < 3:
            raise ValueError("Need at least 3 players to start")

        self.players: list[Player] = []
        for _ in range(0, num_players):
            self.players.append(self.create_random_player())

        self.has_played = False

    @staticmethod
    def create_random_player() -> Player:
        strategy_type = randint(0, 3)
        match strategy_type:
            case 0:
                card_threshold = randint(1, 7)
                strategy = CardCount(card_threshold)

            case 1:
                score_threshold = randint(1, 63)
                include_modifiers = randint(0, 1)
                strategy = ScoreGoal(score_threshold, bool(include_modifiers))

            case 2:
                prob_threshold = uniform(0, 1)
                strategy = RiskTolerance(prob_threshold)

            case 3:
                strategy = MaximumExpectation()

            case _:
                raise ValueError("Bug in Player Creation Logic")

        return Player(strategy)
        

    def play_game(self) -> None:
        if self.has_played:
            raise ValueError("Already Played Game")

        num_rounds = 0
        while any(player.rounds_to_win == -1 for player in self.players):
            # Run a complete round
            self.run_round()
            num_rounds += 1

            # Track players that cross threshold
            for player in self.players:
                if player.total_score >= 200 and player.rounds_to_win == -1:
                    player.rounds_to_win = num_rounds

        self.has_played = True

    def run_round(self):
        # Get a new deck
        round_deck = Deck()
        round_over = False

        # While any player is still in, go around table taking turns
        while not round_over and not all((player.round_state.stay or player.round_state.bust) for player in self.players):
            for player in self.players:
                player.take_turn(round_deck) # TODO: Implement other hand logic

                # Immediately break if any player reaches seven cards
                if len(player.round_state.hand) == 7:
                    round_over = True
                    break


        # Once all players are done or out, tally score and reset
        for player in self.players:
            player.end_round()

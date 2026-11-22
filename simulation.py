from structure import Game
from players import *
import matplotlib.pyplot as plt

def get_mean_rounds(all_players: list[PlayerBase]) -> tuple[list[str], list[float]]:
    counts_dict: dict[str, list[int]] = {}
    for player in all_players:
        current_val = counts_dict.get(player.ID, [0, 0])
        current_val[0] += player.rounds_to_win
        current_val[1] += 1

        counts_dict[player.ID] = current_val

    strategies: list[str] = sorted(counts_dict.keys())
    mean_rounds: list[float] = []
    for id in strategies:
        mean_rounds.append((counts_dict[id][0] / counts_dict[id][1]))

    return strategies, mean_rounds

def get_card_count_dist(all_players: list[PlayerBase]):
    counts_dict: dict[int, list[int]] = {}
    for player in all_players:
        if not isinstance(player, CardCountPlayer):
            continue

        current_val = counts_dict.get(player.card_threshold, [0, 0])
        current_val[0] += player.rounds_to_win
        current_val[1] += 1

        counts_dict[player.card_threshold] = current_val

    thresholds = sorted(counts_dict.keys())
    mean_rounds: list[float] = []
    for threshold in thresholds:
        mean_rounds.append(counts_dict[threshold][0] / counts_dict[threshold][1])

    return thresholds, mean_rounds

def get_score_count_dist(all_players: list[PlayerBase]):
    counts_dict: dict[int, list[int]] = {}
    for player in all_players:
        if not isinstance(player, ScorePlayer):
            continue

        current_val = counts_dict.get(player.score_threshold, [0, 0])
        current_val[0] += player.rounds_to_win
        current_val[1] += 1

        counts_dict[player.score_threshold] = current_val

    thresholds = sorted(counts_dict.keys())
    mean_rounds: list[float] = []
    for threshold in thresholds:
        mean_rounds.append(counts_dict[threshold][0] / counts_dict[threshold][1])

    return thresholds, mean_rounds

if __name__ == "__main__":
    num_games = 1000
    num_players = 3
    log_interval = num_games / 10

    all_players: list[PlayerBase] = []
    for i in range(num_games):
        if i % log_interval == 0:
            print(f"Game {i}")

        game = Game(num_players)
        game.play_game()
        all_players.extend(game.players)

    strategies, overall_mean_rounds = get_mean_rounds(all_players)
    card_thresholds, card_mean_rounds = get_card_count_dist(all_players)
    score_thresholds, score_mean_rounds = get_score_count_dist(all_players)

    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].bar(strategies, overall_mean_rounds)
    ax[0].set_title(f"Overall Average Rounds to Win")
    ax[0].set_ylabel("Rounds")

    ax[1].bar(card_thresholds, card_mean_rounds)
    ax[1].set_title("Average Rounds by Card Goal")
    ax[1].set_ylabel("Rounds")

    ax[2].bar(score_thresholds, score_mean_rounds)
    ax[2].set_title("Average Rounds by Score Goal")
    ax[2].set_ylabel("Rounds")

    fig.suptitle(f"Results for {num_games} games of {num_players} players")

    plt.tight_layout() 
    plt.show()



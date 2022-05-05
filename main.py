from game import Game
from player import Player

def main():
    game = Game(
        player_count=4,
        strategies=[
            [1],
            [1],
            [1, 2],
            [1, 2],
        ]
    )
    game.play_rounds(100)
    game.view_scorecard()


if __name__ == "__main__":
    main()

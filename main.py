from game import Game
from test import test_diversity

test_diversity()

def main():
    game = Game(4)
    game.play_rounds(100)
    game.view_scorecard()

if __name__ == '__main__':
    main()
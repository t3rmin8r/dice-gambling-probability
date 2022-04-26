from game import Game


def test_diversity():
    test_game = Game(4)

    test_game.play_rounds(100)

    for player in range(test_game.player_count):
        score = test_game.scorecard[player]
        assert score['wins'] != 100 and score['ties'] != 100



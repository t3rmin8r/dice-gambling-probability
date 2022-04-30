from game import Game


def test_diversity():
    test_game = Game(4)

    test_game.play_rounds(100)

    for player in range(test_game.player_count):
        score = test_game.scorecard[player]
        assert score["wins"] != 100 and score["ties"] != 100

def test_die_reset():
    test_game = Game(4)

    test_game.play_rounds(2)

    for player in test_game.players:
        assert len(player.holding_die) <= 6 and len(player.rollable_die) <= 6
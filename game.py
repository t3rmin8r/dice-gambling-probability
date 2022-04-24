from hand import Hand

class Game:
    def __init__(self, player_count: int):
        self.player_count = player_count
        self.players = [Hand(x) for x in range(self.player_count)]
#        for player in self.players:
        self.scorecard = self.generate_scorecard()

    def generate_scorecard(self):
        scorecard = {}
        for player in self.players:
            scorecard[player.uid] = {
                    'wins': 0,
                    'ties': 0,
            }
        return scorecard

    def record_score(self, winners):
        if isinstance(winners, list):
            for player in winners:
                self.scorecard[player.uid]['ties'] += 1
        else:
            self.scorecard[winners.uid]['wins'] += 1

    def view_scorecard(self):
        for player in self.scorecard.items():
            print(player)

    def view_players(self):
        if len(self.players) > 0:
            for player in self.players:
                print(player)
        else:
            print("No players!")

    def play_round(self):
        for player in self.players:
            player.generate()
            player.play_round()

        winners = self.get_winner()
        self.record_score(winners)

    def play_rounds(self, count):
        for _ in range(count):
            self.play_round()

    def get_winner(self) -> list or Hand:
        lowest_scorer = None
        winners = []

        for player in self.players:
            if not lowest_scorer:
                lowest_scorer = player
            if player < lowest_scorer:
                lowest_scorer = player

        winners.append(lowest_scorer)

        # Check for ties
        for player in self.players:
            if player == lowest_scorer:
                winners.append(player)

        if len(winners) == 1:
            winners = winners[0]

        return winners
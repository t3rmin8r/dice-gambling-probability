from game import Game

def main():
    game = Game(4)
    
    game.play_rounds(100)
    game.view_scorecard()

if __name__ == '__main__':
    main()
"""
Python terminal version for popular tic tac toe game.

Game is oriented for two players: x and o.
"""

RULES = """
RULES FOR TIC-TAC-TOE

1. The game is played on a grid that's 3 squares by 3 squares.
2. You are X, your friend (or the computer in this case) is O.
Players take turns putting their marks in empty squares.
3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over.
If no player has 3 marks in a row, the game ends in a tie.
"""


class GameOn:

    def __init__(self):
        self.p_signs = 'xo'
        self.p_moves = '123456789'
        self.moves = {
            '1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
            }

    def current_battlefield(self):
        print(f"\n {self.moves['1']} | {self.moves['2']} | {self.moves['3']} ")
        print('-----------')
        print(f" {self.moves['4']} | {self.moves['5']} | {self.moves['6']} ")
        print('-----------')
        print(f" {self.moves['7']} | {self.moves['8']} | {self.moves['9']} \n")

    def play_round(self, player_symbol):
        move = (input("Please select position for next move, from 1 to 9, don't use number "
                      "which is already taken: "))
        if move not in self.p_moves or len(move) != 1:
            print('Ops! You chose wrong symbol or already taken, try again!\n')
            return True
        else:
            self.p_moves = self.p_moves.replace(move, "")
            self.moves[move] = player_symbol
            self.current_battlefield()
            return False

    def win(self, symbol):
        winning_list = [
            ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
            ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
            ['1', '5', '8'], ['3', '5', '7']
        ]
        keys = [k for k, v in self.moves.items() if v == symbol]
        for trio in winning_list:
            success = 0
            for k in trio:
                success += 1 if k in keys else 0
                if success == 3:
                    return True
        return False

    def game(self):
        print('Now first player will choose symbol.')
        while True:
            try:
                player_now = input("Please pick 'X' or 'O': ").lower()
                assert player_now in self.p_signs
                player_later = self.p_signs.replace(player_now, '')
                break
            except AssertionError:
                print('Provided sign is not X or O. Try again!\n')

        while True:
            round_on = True
            print(f"Player with '{player_now}' symbol is now playing.")
            while round_on:
                round_on = self.play_round(player_now)

            if self.win(player_now):
                print(f"Winner is player with '{player_now}' symbol!!!")
                GameOff().start(True)

            if len(self.p_moves) == 0:
                print('We have draw, start game again!')
                GameOff().start(True)

            temporary_player = player_now
            player_now = player_later
            player_later = temporary_player


class GameOff:

    def __init__(self):
        pass

    def start(self, reply=False):
        if not reply:
            while True:
                try:
                    char = input('To start game enter "s" or "p", '
                                 'if you want see the rules enter "r". Have fun!: ').lower()
                    assert char in 'spr'
                    break
                except AssertionError:
                    print('Provided sign is not R or P or S. Try again to play or go away!!\n')
            if char == 'r':
                self.rules()
                GameOff().start()
            else:
                GameOn().game()
        else:
            char = input('Do you want to play again? Enter "y" or "p", if not enter anything else '
                         'and game will stop: ').lower()
            if char == 'y' or char == 'p':
                GameOn().game()
            else:
                raise SystemExit

    def rules(self):
        print('Rules of the game')
        print(RULES)
        print('Battlefield look like that!')
        print(f'\n 1 | 2 | 3 ')
        print('-----------')
        print(f' 4 | 5 | 6 ')
        print('-----------')
        print(f' 7 | 8 | 9 \n')


if __name__ == "__main__":
    print('Welcome to my TicTacToe game!')
    GameOff().start()

"""
Python terminal version for popular tic tac toe game.

Game is oriented for two players: x and o.

RULES FOR TIC-TAC-TOE

1. The game is played on a grid that's 3 squares by 3 squares.

2. You are X, your friend (or the computer in this case) is O.
Players take turns putting their marks in empty squares.

3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4. When all 9 squares are full, the game is over.
If no player has 3 marks in a row, the game ends in a tie.
"""

# import argparse
#
# parser = argparse.ArgumentParser(
#     description='''
#         My help
#     ''',
#     epilog="""All's well that ends well.""")
# # parser.add_argument('--foo', type=int, default=42, help='FOO!')
# # parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
# args = parser.parse_args()


class TicTacToeGame:

    def __init__(self):
        self.p_signs = 'xo'
        self.p_moves = '123456789'
        self.moves = {
            '1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
            }

    def battlefield(self):
        # plansza
        print('Battlefield look like that!')
        print(f'\n 1 | 2 | 3 ')
        print('-----------')
        print(f' 4 | 5 | 6 ')
        print('-----------')
        print(f' 7 | 8 | 9 \n')

    def rules(self):
        # rules
        print('Rules of the game')

    def play_round(self, player):
        # wejscie do gry
        print(f"Player with '{player}' symbol is now playing.")

        # wybranie pola przez 1 gracza

        # sprawdzenie czy wygrane

    def win(self):
        pass

    def game_on(self):
        print('Welcome to my game! Let\'s start with some rules.')
        self.battlefield()

        print('Now first player will choose symbol.')
        while True:
            try:
                # zastanowic sie jak wybierac graczy
                a = input("Please pick 'X' or 'O': ").lower()
                assert a in self.p_signs
                b = self.p_signs.replace(a, '')
                break
            except AssertionError:
                print('Provided sign is not X or O. Try again')

        while True:
            self.play_round(a)

            if self.win():
                break

            t = a
            a = b
            b = t

            break

    def game_off(self):
        # tutaj może coś w stylu czy chcesz zagrać czy zobaczyć zasady najpierw?
        pass


# while sign not in patt:
#     sign = input("Please pick 'X' or 'O': ").lower()
# drugi = patt.replace(sign, '')
#
#
# while True:
#     move = '0'
#     print(f"Player with '{sign}' symbol is now playing.")
#     while (move not in pattern or len(move) != 1):
#         move = (input
#             ("Please select position for next move, from 1 to 9,
#             don't use number which is already taken: "))
#     pattern = pattern.replace(move, "")
#     move_dict[move] = sign
#     print(f"\n {move_dict['1']} | {move_dict['2']} | {move_dict['3']} ")
#     print('-----------')
#     print(f" {move_dict['4']} | {move_dict['5']} | {move_dict['6']} ")
#     print('-----------')
#     print(f" {move_dict['7']} | {move_dict['8']} | {move_dict['9']} \n")
#
#     if move_dict['1'] == move_dict['2'] and move_dict['1'] == move_dict['3'] and move_dict['1'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     elif move_dict['1'] == move_dict['4'] and move_dict['1'] == move_dict['7'] and move_dict['1'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     elif move_dict['1'] == move_dict['5'] and move_dict['1'] == move_dict['9'] and move_dict['1'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     elif move_dict['7'] == move_dict['5'] and move_dict['7'] == move_dict['3'] and move_dict['7'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     if move_dict['2'] == move_dict['5'] and move_dict['2'] == move_dict['8'] and move_dict['2'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     elif move_dict['3'] == move_dict['6'] and move_dict['3'] == move_dict['9'] and move_dict['3'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     if move_dict['4'] == move_dict['5'] and move_dict['4'] == move_dict['6'] and move_dict['4'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     elif move_dict['7'] == move_dict['8'] and move_dict['7'] == move_dict['9'] and move_dict['7'] != ' ':
#         print(f"Winner is player with '{sign}' symbol!!!")
#         break
#     elif len(pattern) == 0:
#         print('We have draw, start game again!')
#         break
#
#     temp = sign
#     sign = drugi
#     drugi = temp

if __name__ == "__main__":
    TicTacToeGame().game_on()

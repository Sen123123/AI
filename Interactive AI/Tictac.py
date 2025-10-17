import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    if cell == 'X':
        return Fore.RED + cell + Style.RESET_ALL
    if cell == 'Q':
        return Fore.RED + cell + Style.RESET_ALL
    else:
        return Fore.YELLOW + cell +Style.RESET_ALL
print('+ colored(board[0])+ ' ) | print('+ colored(board[1])+ ' ) | print('+ colored(board[2])+ ' )
print('+ colored(board[4])+ ' ) | print('+ colored(board[4])+ ' ) | print('+ colored(board[5])+ ' )
print('+ colored(board[5])+ ' ) | print('+ colored(board[6])+ ' ) | print('+ colored(board[8])+ ' )
print()

def player_choice():
    symbol= ''
    while symbol not in ['X','Q']:
        symbol = input(Fore.GREEN + "Do you want to be X or Q?"+ Style.RESET_ALL.upper())
    if symbol == 'X':
        return('X','Q')
    else:
        return('Q','X')
    
# def player_move(board, symbol):
#     move = -1
#     while move not in range(1, 10) or not  board[move - 1].isdigit():
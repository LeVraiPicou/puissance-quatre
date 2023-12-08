import numpy as np

def create_board():
    return np.zeros((6, 7), dtype=int)

def print_board(board):
    for i in board:
        print("|", end=" ")
        for col in i:
            if col == 0:
                print(" ", end=" ")
            elif col == 1:
                print("O", end=" ")
            elif col == 2:
                print("X", end=" ")
        print("|")
    print("+" + "- " * 7 + "+")
    print("| 1 2 3 4 5 6 7 |")

def drop_piece(board, col, player):
    for i in range(5, -1, -1):
        if board[i][col] == 0:
            board[i][col] = player
            break

def is_valid_location(board, col):
    if col > 7 or col < 0:
        return False
    return board[0][col] == 0

def winning_move(board, player):
    for i in range(6):
        for col in range(4):
            if board[i][col] == player and board[i][col + 1] == player and board[i][col + 2] == player and board[i][col + 3] == player:
                return True

    for i in range(3):
        for col in range(7):
            if (
                board[i][col] == player
                and board[i + 1][col] == player
                and board[i + 2][col] == player
                and board[i + 3][col] == player
            ):
                return True

    for i in range(3):
        for col in range(4):
            if (
                board[i][col] == player
                and board[i + 1][col + 1] == player
                and board[i + 2][col + 2] == player
                and board[i + 3][col + 3] == player
            ):
                return True

    for i in range(3):
        for col in range(3, 7):
            if (
                board[i][col] == player
                and board[i + 1][col - 1] == player
                and board[i + 2][col - 2] == player
                and board[i + 3][col - 3] == player
            ):
                return True

    return False

def reverse_board(board):
    cpt_row = 0
    for i in range (len(board[0])):
        tmp_line = []
        for j in range (len(board)):
            if board[j][i] > 0:
                tmp_line.append(board[j][i])
        tmp_line = list(reversed(tmp_line))
        if (len(tmp_line) - 1)//2 == 0:
            tmp = board[(len(board) - 1 - (len(tmp_line) - 1))][cpt_row] 
            board[(len(board) - 1 - (len(tmp_line) - 1))][cpt_row] = board[len(board) - (len(tmp_line) - 1)][cpt_row]
            board[len(board) - (len(tmp_line) - 1)][cpt_row] = tmp
            continue
        for i in range ((len(tmp_line))//2):
            tmp = board[(len(board) - 1 - (len(tmp_line) - 1)) + i][cpt_row] 
            board[(len(board) - 1 - (len(tmp_line) - 1)) + i][cpt_row] = board[len(board) - 1 - i][cpt_row]
            board[len(board) - 1 - i][cpt_row] = tmp
        cpt_row += 1
    return board

def play_game():
    board = create_board()
    game_over = False
    player = 1
                
    print()
    print("=============puisance4=============")
    print("Joueur 1: O / Joueur 2: X")
    print("===================================")
    print()

    while not game_over:
        print_board(board)
        move = input(f"Joueur {player}, choisissez une colonne (1-7) ou tapez 'reverse' pour inverser le plateau : ")
        try:
            if int(move):
                col = int(move) - 1
                if is_valid_location(board, col):
                    drop_piece(board, col, player)
                    if winning_move(board, player):
                        print_board(board)
                        print(f"Le Joueur {player} a gagné !")
                        game_over = True
                    elif np.all(board != 0):
                        print_board(board)
                        print("Match nul !")
                        game_over = True 
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                else:
                    print()
                    print ("Saisie incorrect veuillez réessayer.")
                    print()
        except ValueError:   
            if move.lower() == 'reverse':
                board = reverse_board(board)
                print()
                print("Plateau inversé !")
                print()
            else:
                print()
                print ("Saisie incorrect veuillez réessayer.")
                print()


if __name__ == "__main__":
    play_game()
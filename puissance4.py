import numpy as np

def create_board():
    return np.zeros((6, 7), dtype=int)

def print_board(board):
    for row in board:
        print("|", end=" ")
        for col in row:
            if col == 0:
                print(" ", end=" ")
            elif col == 1:
                print("X", end=" ")
            elif col == 2:
                print("O", end=" ")
        print("|")
    print("+" + "- " * 7 + "+")
    print("| 1 2 3 4 5 6 7 |")

def drop_piece(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            break

def is_valid_location(board, col):
    return board[0][col] == 0

def winning_move(board, player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row][col + 1] == player
                and board[row][col + 2] == player
                and board[row][col + 3] == player
            ):
                return True

    # Check vertical
    for row in range(3):
        for col in range(7):
            if (
                board[row][col] == player
                and board[row + 1][col] == player
                and board[row + 2][col] == player
                and board[row + 3][col] == player
            ):
                return True

    # Check diagonals (positive slope)
    for row in range(3):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row + 1][col + 1] == player
                and board[row + 2][col + 2] == player
                and board[row + 3][col + 3] == player
            ):
                return True

    # Check diagonals (negative slope)
    for row in range(3):
        for col in range(3, 7):
            if (
                board[row][col] == player
                and board[row + 1][col - 1] == player
                and board[row + 2][col - 2] == player
                and board[row + 3][col - 3] == player
            ):
                return True

    return False

def reverse_board(board):
    return np.flipud(board)

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        print_board(board)

        if turn % 2 == 0:
            move = input("Joueur 1 (X), choisissez une colonne (1-7) ou tapez 'reverse' pour inverser le plateau : ")
            if move.lower() == 'reverse':
                board = reverse_board(board)
                print("Plateau inversé !")
                continue
            col = int(move) - 1
            player = 1
        else:
            move = input("Joueur 2 (O), choisissez une colonne (1-7) ou tapez 'reverse' pour inverser le plateau : ")
            if move.lower() == 'reverse':
                board = reverse_board(board)
                print("Plateau inversé !")
                continue
            col = int(move) - 1
            player = 2

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

            turn += 1

if __name__ == "__main__":
    play_game()

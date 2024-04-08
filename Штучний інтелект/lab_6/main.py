import random

# Функція для відображення полі гри
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Функція для створення нового пустого поля гри
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Функція для перевірки, чи є переможець
def check_winner(board, player):
    # Перевірка рядків та стовпців
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Перевірка діагоналей
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Функція для отримання списку можливих ходів
def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Функція для ходу гравця
def player_move(board):
    while True:
        row = int(input("Введіть номер рядка (0, 1, або 2): "))
        col = int(input("Введіть номер стовпця (0, 1, або 2): "))
        if (row, col) in get_possible_moves(board):
            return row, col
        else:
            print("Недопустимий хід. Спробуйте знову.")

# Функція для ходу комп'ютера
def computer_move(board):
    _, move = minimax(board, 0, True)
    return move

# Алгоритм Мінімакс
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth, None
    elif check_winner(board, "X"):
        return depth - 10, None
    elif len(get_possible_moves(board)) == 0:
        return 0, None

    if is_maximizing:
        best_score = -float("inf")
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "O"
            score, _ = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float("inf")
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "X"
            score, _ = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

# Головна функція для виконання гри
def main():
    board = initialize_board()
    display_board(board)

    computer_starts = input("Хто починає перший? (комп'ютер (C) або гравець (P)): ").upper() == "C"
    if computer_starts:
        print("Комп'ютер починає перший.")
    else:
        print("Гравець починає перший.")

    while True:
        if computer_starts:
            # Хід комп'ютера
            print("Хід комп'ютера...")
            computer_row, computer_col = computer_move(board)
            board[computer_row][computer_col] = "O"
            display_board(board)
            if check_winner(board, "O"):
                print("Комп'ютер переміг!")
                break
            if len(get_possible_moves(board)) == 0:
                print("Нічия!")
                break

        # Хід гравця
        player_row, player_col = player_move(board)
        board[player_row][player_col] = "X"
        display_board(board)
        if check_winner(board, "X"):
            print("Гравець переміг!")
            break
        if len(get_possible_moves(board)) == 0:
            print("Нічия!")
            break

        if not computer_starts:
            # Хід комп'ютера
            print("Хід комп'ютера...")
            computer_row, computer_col = computer_move(board)
            board[computer_row][computer_col] = "O"
            display_board(board)
            if check_winner(board, "O"):
                print("Комп'ютер переміг!")
                break
            if len(get_possible_moves(board)) == 0:
                print("Нічия!")
                break

if __name__ == "__main__":
    main()

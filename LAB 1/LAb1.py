import random
import numpy as np

board = [["-"] * 3 for _ in range(3)]

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return True

    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True

    return False

def full():
    return all(cell != "-" for row in board for cell in row)

def can_win(m):
    for i in range(3):
        row = board[i]
        if row.count(m) == 2 and row.count("-") == 1:
            return (i, row.index("-"))

    for i in range(3):
        col = [board[j][i] for j in range(3)]
        if col.count(m) == 2 and col.count("-") == 1:
            return (col.index("-"), i)

    diag1 = [board[i][i] for i in range(3)]
    if diag1.count(m) == 2 and diag1.count("-") == 1:
        return (diag1.index("-"), diag1.index("-"))

    diag2 = [board[i][2 - i] for i in range(3)]
    if diag2.count(m) == 2 and diag2.count("-") == 1:
        return (diag2.index("-"), 2 - diag2.index("-"))

    return None

def display():
    print(np.array(board))

while True:
    display()
    u = tuple(map(int, input("Enter row and column for X (0-2): ").strip().split()))
    if board[u[0]][u[1]] != "-":
        print("Invalid move, try again.")
        continue

    board[u[0]][u[1]] = "X"

    if check_win():
        display()
        print("X wins!")
        break

    if full():
        display()
        print("It's a tie!")
        break
    
    
    move = can_win("O")
    print(move)
    if move is None:
        move = can_win("X")
        if move is None:
            empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == "-"]
            move = random.choice(empty)
    if board[1][1]=="-":
        move=(1 ,1)
    board[move[0]][move[1]] = "O"

    if check_win():
        display()
        print("O wins!")
        break


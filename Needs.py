import random


def print_board(li: list):
    print("\n\n")
    for i in range(len(li)):
        for val in range(len(li[i])):
            print("|\t", li[i][val], end="\t\t")
        print()


def remove_val(val: int, bo: list):
    for i in range(0, len(bo)):
        if val in bo[i]:
            bo[i][bo[i].index(val)] = "X"


def check_win(board):
    count = 0
    for i in range(len(board)):
        is_true = True
        for j in range(len(board)):
            if board[i][j] != "X":
                is_true = False
        if is_true:
            count += 1
    return count + vertical_check(board) + diagonal_check(board)


def vertical_check(board):
    count = 0
    for i in range(len(board)):
        is_true = True
        for j in range(len(board)):
            if board[j][i] != "X":
                is_true = False
        if is_true:
            count += 1
    return count


def diagonal_check(board):
    is_true = True
    count = 0
    for i in range(len(board)):
        if board[i][i] != "X":
            is_true = False
    if is_true:
        count += 1
    is_true = True
    for i in range(len(board)):
        if board[i][4 - i] != 'X':
            is_true = False
    if is_true:
        count += 1

    return count

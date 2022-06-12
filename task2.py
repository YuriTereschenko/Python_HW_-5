# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её,
# причем чтобы сыграть в нее можно было в одиночку.
import random

play_board = ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]


def print_board(board, text):
    print(text)
    for k in range(0, len(board)):
        print(board[k])
    print("-------------------")


def make_turn(board):
    col = int(input("Enter the column number\t")) - 1
    row = int(input("Enter the row number\t")) - 1
    while True:
        if board[row][col] == "[ ]":
            board[row][col] = ' X '
            break
        else:
            print("You can't put your mark here")
            col = int(input("Enter the column number\t"))
            row = int(input("Enter the row number\t"))
    print_board(board, "your turn:")
    return board


def count_score(board):
    for i in range(0, 3):
        x_score = 0
        o_score = 0
        for j in range(0, 3):
            if board[i][j] == " X ":
                x_score += 1
            elif board[i][j] == " O ":
                o_score += 1
        check_win(x_score, o_score)

    for i in range(0, 3):
        x_score = 0
        o_score = 0
        for j in range(0, 3):
            if board[j][i] == " X ":
                x_score += 1
            elif board[j][i] == " O ":
                o_score += 1
    check_win(x_score, o_score)

    x_score = 0
    o_score = 0
    for i in range(0, 3):
        if board[i][i] == " X ":
            x_score += 1
        elif board[i][i] == " O ":
            o_score += 1
    check_win(x_score, o_score)

    x_score = 0
    o_score = 0
    for i in range(0, 3):
        if board[2 - i][i] == " X ":
            x_score += 1
        elif board[2 - i][i] == " O ":
            o_score += 1
    check_win(x_score, o_score)


def check_win(x_score, o_score):
    if x_score == 3:
        print("'X' WIN's!!!")
        exit(0)
    elif o_score == 3:
        print("'O' WIN's!!!")
        exit(0)


def bot_turn(board):
    available_turns = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == "[ ]":
                available_turns.append([i, j])
    turn = available_turns[random.randint(0, len(available_turns) - 1)]
    board[turn[0]][turn[1]] = " O "
    print_board(board, "bot's turn")
    return board


while True:
    play_board = make_turn(play_board)
    count_score(play_board)
    play_board = bot_turn(play_board)
    count_score(play_board)

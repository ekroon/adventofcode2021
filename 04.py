import sys
import os.path as ospath
import math


def mark_number_board(board, number):
    for y, line in enumerate(board):
        for x, board_number in enumerate(line):
            if board_number == number:
                board[y][x] = None


def is_winning_board(board):
    for loop_nr, line in enumerate(board):
        if not [number for number in line if number is not None]:
            return True
        if loop_nr == 0:
            for x in range(len(line)):
                all_none = True
                for y in range(len(board)):
                    if board[y][x] is not None:
                        all_none = False
                        continue
                if all_none:
                    return True


def calculate_board_score(board):
    score = 0
    for line in board:
        for number in line:
            if number:
                score += number
    return score


def solve(numbers, boards):
    winners = []
    scores = []
    for number in numbers:
        for idx, board in enumerate(boards):
            if not idx in winners:
                mark_number_board(board, number)
                if is_winning_board(board):
                    winners.append(idx)
                    scores.append(number * calculate_board_score(board))
    return scores[0], scores[-1]


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = [int(number) for number in lines[0].split(",")]

    boards = []
    board = []
    for line in lines[2:]:
        if line:
            board.append([int(number) for number in line.split()])
        else:
            boards.append(board)
            board = []
    if board:
        boards.append(board)
        board = []

    results = solve(numbers, boards)
    print(results[0])
    print(results[1])

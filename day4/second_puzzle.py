import numpy as np

from first_puzzle import *


def get_last_bingo_board(boards, score_boards, moves):
    number_of_boards = boards.shape[0]
    bingo_indexes = []
    for move in moves:
        for idx, board in enumerate(boards):
            score_boards[idx] = check_if_number_in_board(np.copy(board), np.copy(score_boards[idx]), move)
        for idx, score_board in enumerate(score_boards):
            bingo = check_if_bingo(np.copy(score_board))
            if bingo and idx not in bingo_indexes:
                bingo_indexes.append(idx)
        if len(bingo_indexes) == number_of_boards:
            return get_board_sum(np.copy(boards[bingo_indexes[-1]]),
                                 np.copy(score_boards[bingo_indexes[-1]]), move)
    return 'Did not find bingo, sad!'


def main():
    filename = "input4.txt"
    with open(filename, 'r') as f:
        input_array = f.readlines()

    moves = input_array[0].rstrip("\n").split(",")
    boards = filter_out_boards(input_array[2:])
    score_boards = np.zeros(boards.shape)
    print(get_last_bingo_board(np.copy(boards), np.copy(score_boards), moves))


if __name__ == "__main__":
    main()
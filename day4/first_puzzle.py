import numpy as np


def filter_out_boards(string_boards):
    boards = []
    new_board = np.zeros([5, 5])
    row_index = 0
    for idx, line in enumerate(string_boards):
        if line == "\n":
            boards.append(np.copy(new_board))
            new_board = np.zeros([5, 5])
            row_index = 0
        else:
            line = line.strip("\n")
            split_line = [element for element in line.split(" ") if element]
            new_board[row_index, :] = split_line
            row_index += 1
    # Append the last board
    boards.append(np.copy(new_board))

    return np.array(boards)


def check_if_bingo(board):

    board_shape = 5
    # Check rows
    for row in board:
        if sum(row) == board_shape:
            return True
    # Check columns
    for column in board.T:
        if sum(column) == board_shape:
            return True
    return False


def check_if_number_in_board(board, score_board, move):

    rows, columns = np.where(board == int(move))
    if len(rows):
        for idx, _ in enumerate(rows):
            score_board[rows[idx], columns[idx]] = 1
    return score_board


def evaluate_boards(boards, score_boards, moves):

    for move in moves:
        for idx, board in enumerate(boards):
            score_boards[idx] = check_if_number_in_board(np.copy(board), np.copy(score_boards[idx]), move)
        for idx, score_board in enumerate(score_boards):
            bingo = check_if_bingo(np.copy(score_board))
            if bingo:
                return get_board_sum(np.copy(boards[idx]), np.copy(score_board), move)
    return 'Did not find bingo, sad!'


def get_board_sum(board, score_board, move):
    rows, columns = np.where(score_board == 0)
    total_sum = 0
    if len(rows):
        for idx, _ in enumerate(rows):
            total_sum += board[rows[idx], columns[idx]]
    return total_sum * int(move)


def main():

    filename = "input4.txt"
    with open(filename, 'r') as f:
        input_array = f.readlines()

    moves = input_array[0].rstrip("\n").split(",")
    boards = filter_out_boards(input_array[2:])
    score_boards = np.zeros(boards.shape)
    print(evaluate_boards(np.copy(boards), np.copy(score_boards), moves))


if __name__ == "__main__":
    main()

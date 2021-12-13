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

    # Check rows
    for row in board:
        if ''.join(element for element in row) == 'XXXXX':
            return True, board
    # Check columns
    for column in board.T:
        if ''.join(element for element in column) == 'XXXXX':
            return True, board
    return False, board


def main():

    filename = "input4.txt"
    with open(filename, 'r') as f:
        input_array = f.readlines()

    moves = input_array[0]
    boards = filter_out_boards(input_array[2:])


if __name__ == "__main__":
    main()

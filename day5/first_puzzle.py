import numpy as np
from grid import Grid


def format_input_line(lines):
    starts = []
    ends = []

    for line in lines:
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        starts.append([int(x1), int(y1)])
        ends.append([int(x2), int(y2)])

    return starts, ends


def get_grid(starts, ends):
    max_numb = np.max([starts, ends])
    return np.zeros((max_numb, max_numb))


def main():
    filename = "input5.txt"
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    starts, ends = format_input_line(lines)
    my_grid = Grid(starts=starts, ends=ends)
    my_grid.add_lines_to_grid()
    print(my_grid.get_number_above_threshold())
    print("")


if __name__ == "__main__":
    main()

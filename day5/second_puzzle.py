from first_puzzle import *


def main():
    filename = "input5.txt"
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    starts, ends = format_input_line(lines)
    my_grid = Grid(starts=starts, ends=ends)
    my_grid.add_all_lines_to_grid()
    print(my_grid.get_number_above_threshold())


if __name__ == "__main__":
    main()

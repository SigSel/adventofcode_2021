import math


def check_neighbours(row, column, grid):
    smaller = 0
    neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    number = int(grid[row][column])
    for r, c in neighbours:
        if row + r == -1 or column + c == -1:
            smaller += 1
            continue
        try:
            neighbour = int(grid[row + r][column + c])
        except IndexError:
            neighbour = 9999
            pass
        if number < neighbour:
            smaller += 1

    return True if smaller == len(neighbours) else False


def get_sum(points):
    total = 0

    for point in points:
        total += int(point)

    return total + len(points)


def find_basin(row, column, grid, visited_index, row_length, column_length):
    if row < 0 or column < 0 or row > row_length or column > column_length or grid[row][column] == "9" \
            or (row, column) in visited_index:
        return

    visited_index.append((row, column))

    find_basin(row+1, column, grid, visited_index, row_length, column_length)
    find_basin(row-1, column, grid, visited_index, row_length, column_length)
    find_basin(row, column+1, grid, visited_index, row_length, column_length)
    find_basin(row, column-1, grid, visited_index, row_length, column_length)


def basins(low_points_index, grid):
    all_basins = []
    row_length = len(grid) - 1
    column_length = len(grid[0]) - 1
    for r, c in low_points_index:
        visited_index = []
        find_basin(r, c, grid, visited_index, row_length, column_length)
        all_basins.append(len(visited_index))

    return math.prod(sorted(all_basins, reverse=True)[0:3])


def main():
    filename = "input9.txt"
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    low_points = []
    low_points_index = []
    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            if check_neighbours(i, j, lines):
                low_points.append(lines[i][j])
                low_points_index.append([i, j])

    print(get_sum(low_points))

    print(basins(low_points_index, lines))


if __name__ == "__main__":
    main()


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


def main():
    filename = "input9.txt"
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    low_points = []
    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            if check_neighbours(i, j, lines):
                low_points.append(lines[i][j])

    print(get_sum(low_points))


if __name__ == "__main__":
    main()

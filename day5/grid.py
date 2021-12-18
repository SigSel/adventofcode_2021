import numpy as np


class Grid:
    def __init__(self, starts, ends):
        self.starts = starts
        self.ends = ends
        self.max_number = np.max([starts, ends])
        self.internal_grid = np.zeros((self.max_number+1, self.max_number+1))

    def add_lines_to_grid(self):
        for idx, _ in enumerate(self.starts):
            x1, y1 = self.starts[idx]
            x2, y2 = self.ends[idx]

            if x1 != x2 and y1 != y2:
                continue
            elif x1 == x2:
                line = list(range(min(y1, y2), max(y1, y2) + 1))
                for i in line:
                    self.internal_grid[x1, i] += 1
            elif y1 == y2:
                line = list(range(min(x1, x2), max(x1, x2) + 1))
                for i in line:
                    self.internal_grid[i, y1] += 1

    def get_number_above_threshold(self, threshold=2):
        count = np.count_nonzero(self.internal_grid >= threshold)
        return count

#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """
    iterates through each cell in the grid, and for each land cell
    (where the value is 1), it increments the perimeter by 4 (since each land cell has 4
    sides)
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter

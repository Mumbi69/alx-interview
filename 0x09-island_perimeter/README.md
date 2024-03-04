# Island Perimeter
* This function iterates through each cell in the grid, and for each land cell (where the value is 1), it increments the perimeter by 4 (since each land cell has 4 sides).
* Then, it checks if the cell has a neighboring land cell to the left or above it and decrements the perimeter accordingly (since adjacent land cells share a side).

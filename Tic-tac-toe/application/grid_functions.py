def get_column(grid, num_of_column):
    if num_of_column == 1:
        return [grid[0], grid[3], grid[6]]
    elif num_of_column == 2:
        return [grid[1], grid[4], grid[7]]
    elif num_of_column == 3:
        return [grid[2], grid[5], grid[8]]
    else:
        raise Exception(f"no such column in a tic-tac-toe grid: {num_of_column}")


def get_row(grid, num_of_row):
    if num_of_row == 1:
        return [grid[0], grid[1], grid[2]]
    elif num_of_row == 2:
        return [grid[3], grid[4], grid[5]]
    elif num_of_row == 3:
        return [grid[6], grid[7], grid[8]]
    else:
        raise Exception(f"no such row in a tic-tac-toe grid: {num_of_row}")


def get_diagonal(grid, num_of_diagonal):
    if num_of_diagonal == 1:
        return [grid[0], grid[4], grid[8]]
    elif num_of_diagonal == 2:
        return [grid[2], grid[4], grid[6]]
    else:
        raise Exception(f"no such diagonal in a tic-tac-toe grid: {num_of_diagonal}")

def get_winner(grid):
    for num_of_column in range(1, 4):
        column = get_column(grid, num_of_column)
        if column[0] == column[1] == column[2]:
            return column[0]

    for num_of_row in range(1, 4):
        row = get_row(grid, num_of_row)
        if row[0] == row[1] == row[2]:
            return row[0]
    
    for num_of_diagonal in range(1, 3):
        diagonal = get_diagonal(grid, num_of_diagonal)
        if diagonal[0] == diagonal[1] == diagonal[2]:
            return diagonal[0]
    
    return 'No winner'
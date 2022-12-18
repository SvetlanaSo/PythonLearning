import grid_functions as gf
import random

def get_valid_turn(char_of_player, grid):
    win_is_possible, winning_grid = check_if_win_is_possible(grid, char_of_player)
    if win_is_possible:
        return winning_grid
    need_to_block, blocking_grid = check_if_need_to_block(grid, char_of_player)
    if need_to_block:
        return blocking_grid
    
    return make_move_to_center_or_corners(grid, char_of_player)

def check_line_if_win_is_possible(line, char_of_player):
    count_char_of_player = 0
    for c in line:
        if c == f'[{char_of_player}]':
            count_char_of_player += 1
    if count_char_of_player == 2:
        if line[0] in '[1], [2], [3], [4], [5], [6], [7], [8], [9]':
            return True, 0
        elif line[1] in '[1], [2], [3], [4], [5], [6], [7], [8], [9]':
            return True, 1
        elif line[2] in '[1], [2], [3], [4], [5], [6], [7], [8], [9]':
            return True, 2
    
    return False, -1

def check_line_if_need_to_block_opponent(line, char_of_player):
    count_char_of_opponent = 0
    for c in line:
        if c != f'[{char_of_player}]' and c not in '[1], [2], [3], [4], [5], [6], [7], [8], [9]':
            count_char_of_opponent += 1
    if count_char_of_opponent == 2:
        if line[0] in '[1], [2], [3], [4], [5], [6], [7], [8], [9]':
            return True, 0
        elif line[1] in '[1], [2], [3], [4], [5], [6], [7], [8], [9]':
            return True, 1
        elif line[2] in '[1], [2], [3], [4], [5], [6], [7], [8], [9]':
            return True, 2

    return False, -1

def make_move_to_center_or_corners(grid: list, char_of_player):
    if grid[4] == '[5]':
        grid[4] = f'[{char_of_player}]'
        return grid
    else:
        array = []
        if grid[0] == '[1]':
            array.append(grid[0])
        if grid[2] == '[3]':
            array.append(grid[2])
        if grid[6] == '[7]':
            array.append(grid[6])
        if grid[8] == '[9]':
            array.append(grid[8])
    if array == []:
        if grid[1] == '[2]':
            array.append(grid[1])
        if grid[3] == '[4]':
            array.append(grid[3])
        if grid[5] == '[6]':
            array.append(grid[5])
        if grid[7] == '[8]':
            array.append(grid[7])
    random_cell = random.choice(array)
    pos = grid.index(random_cell)
    grid[pos] = f'[{char_of_player}]'

    return grid

def check_if_win_is_possible(grid: list, char_of_player: str):
    for num_of_column in range(1, 4):
        column = gf.get_column(grid, num_of_column)
        win_is_possible, cell = check_line_if_win_is_possible(column, char_of_player)
        if win_is_possible:
            index = grid.index(column[cell])
            grid[index] = f'[{char_of_player}]'
            return True, grid
    for num_of_row in range(1, 4):
        row = gf.get_row(grid, num_of_row)
        win_is_possible, cell = check_line_if_win_is_possible(row, char_of_player)
        if win_is_possible:
            index = grid.index(row[cell])
            grid[index] = f'[{char_of_player}]'
            return True, grid
    for num_of_diagonal in range(1, 3):
        diagonal = gf.get_diagonal(grid, num_of_diagonal)
        win_is_possible, cell = check_line_if_win_is_possible(diagonal, char_of_player)
        if win_is_possible:
            index = grid.index(diagonal[cell])
            grid[index] = f'[{char_of_player}]'
            return True, grid

    return False, -1

def check_if_need_to_block(grid: list, char_of_player: str):
    for num_of_column in range(1, 4):
        column = gf.get_column(grid, num_of_column)
        need_to_block, cell = check_line_if_need_to_block_opponent(column, char_of_player)
        if need_to_block:
            index = grid.index(column[cell])
            grid[index] = f'[{char_of_player}]'
            return True, grid
    for num_of_row in range(1, 4):
        row = gf.get_row(grid, num_of_row)
        need_to_block, cell = check_line_if_need_to_block_opponent(row, char_of_player)
        if need_to_block:
            index = grid.index(row[cell])
            grid[index] = f'[{char_of_player}]'
            return True, grid
    for num_of_diagonal in range(1, 3):
        diagonal = gf.get_diagonal(grid, num_of_diagonal)
        need_to_block, cell = check_line_if_need_to_block_opponent(diagonal, char_of_player)
        if need_to_block:
            index = grid.index(diagonal[cell])
            grid[index] = f'[{char_of_player}]'
            return True, grid

    return False, -1
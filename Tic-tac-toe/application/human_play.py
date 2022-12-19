def get_valid_turn(char_of_player, grid):
    turn = input("Enter a cell's digit where you want to go.")
    turn_valid = turn in '123456789' \
        and len(turn) == 1 \
        and grid[int(turn) - 1] != '[0]' \
        and grid[int(turn) - 1] != '[X]'
    while not turn_valid:
        print('Invalid value entered. Enter a digit from 1 to 9 which points to an empty cell.')
        turn = input("Enter a cell's digit where you want to go.")
        turn_valid = turn in '123456789' \
            and len(turn) == 1 \
            and grid[int(turn) - 1] != '[0]' \
            and grid[int(turn) - 1] != '[X]'
    
    grid[int(turn) - 1] = f'[{char_of_player}]'
    return grid
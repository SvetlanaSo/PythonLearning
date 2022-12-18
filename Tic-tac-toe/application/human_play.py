def get_valid_turn(char_of_player, grid):
    turn = input("Enter a cell's digit where you want to go.")
    while turn not in '123456789':
        print('Invalid value entered. Enter a digit from 1 to 9.') 
        turn = input("Enter a cell's digit where you want to go.")
    grid[int(turn) - 1] = f'[{char_of_player}]'
    return grid

import grid_functions
import human_play
import robot_play
import random

def display_result(grid):
    print(grid[0], grid[1], grid[2], sep='')
    print(grid[3], grid[4], grid[5], sep='')
    print(grid[6], grid[7], grid[8], sep='')

def get_player_name(num_of_player):
    name = input(f'Enter name of Player #{num_of_player}.')
    return name

def get_player(player_num):
    player = input(f'Who will be Player #{player_num} - human or robot? Enter "H" for human and "R" for robot.').upper()
    while not (player == 'H' or player == 'R'):
        print('Invalid value entered. Try again')
        player = input('Enter "H" or "R".').upper()
    if player == 'H':
        player_name = get_player_name(player_num)
        strategy = human_play.get_valid_turn
    else:
        player_name = 'Metatron'
        strategy = robot_play.get_valid_turn
    return strategy, player_name


def get_players_reordered_randomly(player1, player2):
    order = [player1, player2]
    random.shuffle(order)
    return order[0], order[1]


def play_game():
    grid = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']
    player1_strategy, player1_name = get_player(1)
    player2_strategy, player2_name = get_player(2)
    print(f'Great! This game will be between Player #1 - {player1_name} and Player #2 - {player2_name}.')

    player1, player2 = get_players_reordered_randomly((player1_strategy, player1_name), (player2_strategy, player2_name))
    print(f'{player1[1]} plays with X, {player2[1]} plays with 0. {player1[1]} plays first.')
    
    display_result(grid)
    there_is_no_winner = True
    turn = 0
    chars = ['X', '0']
    while there_is_no_winner and turn < 9:
        if turn % 2 == 0:
            current_player_strategy = player1[0]
            char_of_player = chars[0]
            print(f"{player1[1]}'s turn to play.")
        else:
            current_player_strategy = player2[0]
            char_of_player = chars[1]
            print(f"{player2[1]}'s turn to play.")
        grid = current_player_strategy(char_of_player, grid)
        display_result(grid)
        winner = grid_functions.get_winner(grid)
        if (winner != 'No winner'):
            if winner == '[0]':
                print(f'congrats, {player2[1]}.')
            else:
                print(f'congrats, {player1[1]}.')
            there_is_no_winner = False
        turn +=1
    if there_is_no_winner:
        print('Draw')

if __name__ == "__main__":
    play_game()
import random
import emoji


def display_board(board):
    print(' ' + board[1] + '||' + board[2] + '||' + board[3])
    print('----------')
    print(' ' + board[4] + '||' + board[5] + '||' + board[6])
    print('----------')
    print(' ' + board[7] + '||' + board[8] + '||' + board[9])
    print('----------')


def player_input():
    marker = ""

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 choose the X or O: ").upper()

    ''' Assign the player 2'''

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False


def choose_first():
    player_list = ('player_1', 'player_2')
    player = random.choices(player_list)
    return player[0]


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    else:
        return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Choose your next position: (1-9) '))
        except:
            print("Integer value can be accepted {}".format("😥:"))

    return position


def replay():
    return input("Do you want to continue Yes or No: ")


def start_game():
    print("Welcome to Tic Tac Toe! {}".format("😎:"))

    while True:
        test_board = [' '] * 10
        print("Start the Game ☺:")
        player_1, player_2 = player_input()
        print("Player 1 is {}".format(player_1))
        print("Player 2 is {}".format(player_2))
        play_game = input("Are you ready to start the game: Yes or No 👍:").upper()
        print("Let's toss for the chance")
        chance = choose_first()
        print("{} has won the toss and you can start 😎:".format(chance))
        if play_game == 'YES' or 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if chance == 'player_1':
                display_board(test_board)
                position = player_choice(test_board)
                print(position)
                place_marker(test_board, player_1, position)

                status = win_check(test_board, player_1)
                if status:
                    display_board(test_board)
                    print("Congratulations You have Won the game {}".format("✌:"))
                    game_on = False
                else:
                    space = full_board_check(test_board)
                    if space:
                        display_board(test_board)
                        print("Hey!! Match has drawn {} ".format("😥:"))
                        break
                    else:
                        chance = 'player_2'

            else:
                display_board(test_board)
                position = player_choice(test_board)
                print(position)
                place_marker(test_board, player_2, position)
                status = win_check(test_board, player_2)
                if status:
                    display_board(test_board)
                    print("Congratulations You have Won the game {}".format("✌:"))
                    game_on = False
                else:
                    space = full_board_check(test_board)
                    if space:
                        display_board(test_board)
                        print("Hey!! Match has drawn {} ".format("😥:"))
                        break
                    else:
                        chance = 'player_1'
        response = replay()
        if response == 'Yes':
            continue
        else:
            break



start_game()

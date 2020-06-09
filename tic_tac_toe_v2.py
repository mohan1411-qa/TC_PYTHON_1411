import random
'''Play the classic Tic-Tac-Toe game (also called Noughts and Crosses) for free'''


'''Method to display the Tic-Tac-Toe board'''


def display_board(board):
    print(' ' + board[1] + '||' + board[2] + '||' + board[3])
    print('----------')
    print(' ' + board[4] + '||' + board[5] + '||' + board[6])
    print('----------')
    print(' ' + board[7] + '||' + board[8] + '||' + board[9])
    print('----------')


'''Method to assign the marker to players'''


def player_input(player_details):
    marker = ""

    while not (marker == 'X' or marker == 'O'):
        marker = input("{} choose the X or O: ".format(player_details['player_1'])).upper()

    ''' Assign the player 2'''

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


'''Method to place the marker'''


def place_marker(board, marker, position):
    board[position] = marker


'''Method to check whether player has won the game'''


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


'''Method to choose the player's turn'''


def choose_first(player_details):
    player_list = (player_details['player_1'], player_details['player_2'])
    player = random.choices(player_list)
    return player[0]


'''Method to check whether position is free to insert the marker'''


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


'''Method to check whether board is full'''


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    else:
        return True


'''Player will choose the position'''


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Choose your next position: (1-9) '))
        except:
            print("Integer value can be accepted {}".format("😥:"))

    return position


'''Player info will be displayed'''


def player_info():
    player_dict = {}

    player_dict["player_1"] = input("Hi player 1 : Please enter your name ☺: ")
    player_dict["player_2"] = input("Hi player 2 : Please enter your name ☺: ")

    return player_dict


def replay():
    return input("Do you want to continue Yes or No: ").upper()


def start_game():
    print("Welcome to Tic Tac Toe! {}".format("😎:"))

    while True:
        player_value = {}
        test_board = [' '] * 10
        print("Start the Game ☺:")
        player_details= player_info()
        player_1, player_2 = player_input(player_details)

        player_value[player_details['player_1']] = player_1
        player_value[player_details['player_2']] = player_2

        print("{} is {}".format(player_details['player_1'], player_value[player_details['player_1']]))
        print("{} is {}".format(player_details['player_2'], player_value[player_details['player_2']]))

        play_game = input("Are you ready to continue the game: Yes or No 👍:").upper()

        print("Let's toss for the turn")
        chance = choose_first(player_details)
        print("Congrats {} you have won the toss and now you can start 😎:".format(chance))

        if play_game == 'YES' or 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if chance == player_details['player_1']:
                display_board(test_board)
                print("{}!! It's your turn".format(chance))
                position = player_choice(test_board)
                print(position)
                place_marker(test_board, player_1, position)

                status = win_check(test_board, player_1)
                if status:
                    display_board(test_board)
                    print("Congratulations !!! Well played {} you have won the game {}".format(chance, "✌:"))
                    print("Hard Luck !!! {} Better Luck Next Time {}".format(player_details['player_2'], "😢:"))
                    game_on = False
                else:
                    space = full_board_check(test_board)
                    if space:
                        display_board(test_board)
                        print("Hey!! Match has drawn {} ".format("😥:"))
                        break
                    else:
                        chance = player_details['player_2']

            else:
                display_board(test_board)
                print("{}!! It's your turn".format(chance))
                position = player_choice(test_board)
                print(position)
                place_marker(test_board, player_2, position)
                status = win_check(test_board, player_2)
                if status:
                    display_board(test_board)
                    print("Congratulations !!! Well played {} you have won the game {}".format(chance, "✌:"))
                    print("Hard Luck !!! {} Better Luck Next Time {}".format(player_details['player_1'], "😢:"))
                    game_on = False
                else:
                    space = full_board_check(test_board)
                    if space:
                        display_board(test_board)
                        print("Hey!! Match has drawn {} ".format("😥:"))
                        break
                    else:
                        chance = player_details['player_1']
        response = replay()
        if response == 'Yes':
            continue
        else:
            break


















test_board = ['#','X','O',' ','O','X','O','X','O','X']
# display_board(test_board)
# player_1, player_2 = player_input()
# place_marker(test_board,'X',8)
# display_board(test_board)
# status = win_check(test_board, 'X')
# print(status)
# chance = choose_first()
# print(chance)
# status = full_board_check(test_board)
# print(status)
start_game()

from copy import deepcopy

main_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player_go = 0
while True:
    player_x_or_o = input("Do you want to be x or o?\n").lower()
    if (player_x_or_o == "x") or (player_x_or_o == "o"):
        break
    else:
        print("Invalid input")
if player_x_or_o == "x":
    computer_x_or_o = "o"
else:
    computer_x_or_o = "x"


def print_board():
    for i in main_board:
        print(str(i).replace("[", "").replace("]", ""))


def is_winner(board_to_check):

    #check horizontally
    for i in board_to_check:
        xs = 0
        os = 0
        for x in i:
            if x == "x":
                xs += 1
            elif x == "o":
                os += 1
        if xs == 3:
            return "x"
        elif os == 3:
            return "o"

    #check verticly
    for i in range(0, 3):
        xs = 0
        os = 0
        for x in range(0, 3):
            if board_to_check[x][i] == "x":
                xs += 1
            elif board_to_check[x][i] == "o":
                os += 1
        if xs == 3:
            return "x"
        elif os == 3:
            return "o"

    #check diagonals
    if (board_to_check[0][0] == "x") and (board_to_check[1][1] == "x") and (board_to_check[2][2] == "x"):
        return "x"
    elif (board_to_check[0][0] == "o") and (board_to_check[1][1] == "o") and (board_to_check[2][2] == "o"):
        return "o"
    if (board_to_check[0][2] == "x") and (board_to_check[1][1] == "x") and (board_to_check[2][0] == "x"):
        return "x"
    elif (board_to_check[0][2] == "o") and (board_to_check[1][1] == "o") and (board_to_check[2][0] == "o"):
        return "o"


def is_players_go():
    return (player_x_or_o == "x" and player_go % 2 == 0) or (player_x_or_o == "o" and player_go % 2 == 1)


def is_x_or_o():
    if player_go % 2 == 0:
        return "x"
    else:
        return "o"


def num_of_spaces(board_to_check_spaces):
    spaces = 0
    for x in board_to_check_spaces:
        for i in x:
            if str(i) == " ":
                spaces += 1
    return spaces


def best(board):
    global board_thats_best

    # Check if the game has a winner
    winner = is_winner(board)
    if winner == "x":
        return 10
    elif winner == "o":
        return -10
    elif num_of_spaces(board) == 0:  # No more moves left
        return 0

    # Identify the current player
    num_of_space_variable = num_of_spaces(board)
    if num_of_space_variable % 2 == 0:
        player = "o"
    else:
        player = "x"

    possible_moves = []
    for num_1 in range(3):
        for num_2 in range(3):
            if board[num_1][num_2] == " ":
                temp_board = deepcopy(board)
                temp_board[num_1][num_2] = player
                possible_moves.append(temp_board)

    final_list = []
    for move in possible_moves:
        final_list.append(best(move))  # Recursive call to evaluate each move

    # Maximize for 'x' and minimize for 'o'
    if player == "x":
        return_value = max(final_list)
        board_thats_best = possible_moves[final_list.index(return_value)]  # Store the best move
    else:
        return_value = min(final_list)
        board_thats_best = possible_moves[final_list.index(return_value)]  # Store the best move

    return return_value


for moves in range(9):
    if is_winner(main_board):
        print(f"{is_winner(main_board).upper()} wins!")
        break


    if is_players_go():
        while True:
            try:
                row = int(input("What row number do you want to go? (1-3)\n")) - 1
                column = int(input("What column number do you want to go? (1-3)\n")) - 1
                if 0 <= row < 3 and 0 <= column < 3:
                    if main_board[row][column] == " ":
                        main_board[row][column] = player_x_or_o
                        break
                    else:
                        print("Space taken.")
                else:
                    print("Invalid input, please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
    else:
        best(main_board)
        main_board = deepcopy(board_thats_best)
        print("Computer made its move.")
    print_board()
    player_go += 1
if (is_winner(main_board) == None) and (num_of_spaces(main_board) == 0):
    print("It's a draw!")

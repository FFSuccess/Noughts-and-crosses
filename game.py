import copy

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player_go = 0
move_value = 0
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
for i in board:
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


def possibilities_level_1(board_to_find_posibilities_l1, player_go_x_or_o_l1):
    global move_value
    boards = []
    for f in range(0, 3):
        for x in range(0, 3):
            if board_to_find_posibilities_l1[f][x] == " ":
                new_board = copy.deepcopy(board_to_find_posibilities_l1)
                new_board[f][x] = player_go_x_or_o_l1
                if is_winner(new_board) == computer_x_or_o:
                    move_value += 1
                elif is_winner(new_board) == player_x_or_o:
                    move_value -= 1
                else:
                    boards.append(new_board)
    return boards


def possibilities_level_1_no_move_value(board_to_find_posibilities_l1, player_go_x_or_o_l1):
    boards = []
    for f in range(0, 3):
        for x in range(0, 3):
            if board_to_find_posibilities_l1[f][x] == " ":
                new_board = copy.deepcopy(board_to_find_posibilities_l1)
                new_board[f][x] = player_go_x_or_o_l1
                boards.append(new_board)
    return boards


def possibilities_level_2(board_to_find_posibilities_l2, player_go_x_or_o_l2):
    global move_value
    boards_level_2 = []
    if player_go_x_or_o_l2 == "x":
        other_l2 = "o"
    else:
        other_l2 = "x"
    for w in possibilities_level_1(board_to_find_posibilities_l2, other_l2):
        boards_level_2 += possibilities_level_1(w, player_go_x_or_o_l2)
    return boards_level_2


def possibilities_level_3(board_to_find_posibilities_l3, player_go_x_or_o_l3):
    global move_value
    boards_level_3 = []
    if player_go_x_or_o_l3 == "x":
        other_l3 = "o"
    else:
        other_l3 = "x"
    for w in possibilities_level_2(board_to_find_posibilities_l3, other_l3):
        boards_level_3 += possibilities_level_1(w, player_go_x_or_o_l3)
    return boards_level_3


def possibilities_level_4(board_to_find_posibilities_l4, player_go_x_or_o_l4):
    global move_value
    boards_level_4 = []
    if player_go_x_or_o_l4 == "x":
        other_l4 = "o"
    else:
        other_l4 = "x"
    for w in possibilities_level_3(board_to_find_posibilities_l4, other_l4):
        boards_level_4 += possibilities_level_1(w, player_go_x_or_o_l4)
    return boards_level_4


def possibilities_level_5(board_to_find_posibilities_l5, player_go_x_or_o_l5):
    global move_value
    boards_level_5 = []
    if player_go_x_or_o_l5 == "x":
        other_l5 = "o"
    else:
        other_l5 = "x"
    for w in possibilities_level_4(board_to_find_posibilities_l5, other_l5):
        boards_level_5 += possibilities_level_1(w, player_go_x_or_o_l5)
    return boards_level_5


def possibilities_level_6(board_to_find_posibilities_l6, player_go_x_or_o_l6):
    global move_value
    boards_level_6 = []
    if player_go_x_or_o_l6 == "x":
        other_l6 = "o"
    else:
        other_l6 = "x"
    for w in possibilities_level_5(board_to_find_posibilities_l6, other_l6):
        boards_level_6 += possibilities_level_1(w, player_go_x_or_o_l6)
    return boards_level_6


def possibilities_level_7(board_to_find_posibilities_l7, player_go_x_or_o_l7):
    global move_value
    boards_level_7 = []
    if player_go_x_or_o_l7 == "x":
        other_l7 = "o"
    else:
        other_l7 = "x"
    for w in possibilities_level_6(board_to_find_posibilities_l7, other_l7):
        boards_level_7 += possibilities_level_1(w, player_go_x_or_o_l7)
    return boards_level_7


def possibilities_level_8(board_to_find_posibilities_l8, player_go_x_or_o_l8):
    global move_value
    boards_level_8 = []
    if player_go_x_or_o_l8 == "x":
        other_l8 = "o"
    else:
        other_l8 = "x"
    for w in possibilities_level_7(board_to_find_posibilities_l8, other_l8):
        boards_level_8 += possibilities_level_1(w, player_go_x_or_o_l8)
    return boards_level_8


def possibilities_level_9(board_to_find_posibilities_l9, player_go_x_or_o_l9):
    global move_value
    boards_level_9 = []
    if player_go_x_or_o_l9 == "x":
        other_l9 = "o"
    else:
        other_l9 = "x"
    for w in possibilities_level_8(board_to_find_posibilities_l9, other_l9):
        boards_level_9 += possibilities_level_1(w, player_go_x_or_o_l9)
    return boards_level_9


def all_possibilities(board_to_find_all_possibilities):
    if num_of_spaces(board_to_find_all_possibilities) == 0:
        return board_to_find_all_possibilities
    if num_of_spaces(board_to_find_all_possibilities) == 1:
        return possibilities_level_1(board_to_find_all_possibilities, "x")
    if num_of_spaces(board_to_find_all_possibilities) == 2:
        return possibilities_level_2(board_to_find_all_possibilities, "o")
    if num_of_spaces(board_to_find_all_possibilities) == 3:
        return possibilities_level_3(board_to_find_all_possibilities, "x")
    if num_of_spaces(board_to_find_all_possibilities) == 4:
        return possibilities_level_4(board_to_find_all_possibilities, "o")
    if num_of_spaces(board_to_find_all_possibilities) == 5:
        return possibilities_level_5(board_to_find_all_possibilities, "x")
    if num_of_spaces(board_to_find_all_possibilities) == 6:
        return possibilities_level_6(board_to_find_all_possibilities, "o")
    if num_of_spaces(board_to_find_all_possibilities) == 7:
        return possibilities_level_7(board_to_find_all_possibilities, "x")
    if num_of_spaces(board_to_find_all_possibilities) == 8:
        return possibilities_level_8(board_to_find_all_possibilities, "o")
    if num_of_spaces(board_to_find_all_possibilities) == 9:
        return possibilities_level_9(board_to_find_all_possibilities, "x")


def best_move():
    global board, move_value
    best_move_value = -99999999999999999999999999999999
    best_possible_move = []
    moves = possibilities_level_1_no_move_value(board, computer_x_or_o)
    for m in moves:
        if is_winner(m) == computer_x_or_o:
            board = copy.deepcopy(m)
            return
    for m in moves:
        move_value = 0
        all_possibilities(m)
        if move_value > best_move_value:
            best_move_value = copy.deepcopy(move_value)
            best_possible_move = copy.deepcopy(m)
    board = copy.deepcopy(best_possible_move)


for moves in range(9):
    if is_winner(board):
        print(f"{is_winner(board).upper()} wins!")
        break
    if (is_winner(board) == None) and (num_of_spaces(board) == 0):
        print("It's a draw!")
        break

    if is_players_go():
        while True:
            try:
                row = int(input("What row number do you want to go? (1-3)\n")) - 1
                column = int(input("What column number do you want to go? (1-3)\n")) - 1
                if 0 <= row < 3 and 0 <= column < 3:
                    if board[row][column] == " ":
                        board[row][column] = player_x_or_o
                        break
                    else:
                        print("Space taken.")
                else:
                    print("Invalid input, please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input, please enter a valid number.")
    else:
        best_move()
        print("Computer made its move.")
    for i in board:
        print(str(i).replace("[", "").replace("]", ""))
    player_go += 1

import sys
import time
from copy import deepcopy
import pygame
import pip


main_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player_go = 0


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


pygame.init()
size = 1080
screen = pygame.display.set_mode((1080, 1080))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
screen.fill(WHITE)
cross = pygame.image.load("output-onlinepngtools(1).png")
nought = pygame.image.load("Untitled drawing(1).png")
screen.blit(cross, (128,366))
screen.blit(nought, (604, 366))
clock.tick()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            #check if cross or nought clicked
            if ((x <= 476) and (x >= 128)) and ((y <= 714) and (y >= 366)):
                player_x_or_o = "x"
                running = False
            if ((x <= 952) and (x >= 604)) and ((y <= 714) and (y >= 366)):
                player_x_or_o = "o"
                running = False


screen.fill(WHITE)
def draw_grid():
    screen.fill(WHITE)
    possitions = (
        ((0, 0), (366, 0), (732, 0)),
        ((0, 366), (366, 366), (732, 366)),
        ((0, 732), (366, 732), (732, 732))
    )
    pygame.draw.rect(screen, BLACK, (348 ,0 ,18, 1080))
    pygame.draw.rect(screen, BLACK, (708 ,0 ,18, 1080))
    pygame.draw.rect(screen, BLACK, (0 ,348 ,1080, 18))
    pygame.draw.rect(screen, BLACK, (0 ,708 ,1080, 18))
    for index_1, i_1 in enumerate(main_board):
        for index_2, i_2 in enumerate(i_1):
            if i_2 == "x":
                x, y = possitions[index_1][index_2][0], possitions[index_1][index_2][1]
                screen.blit(cross, (x, y))
            elif i_2 == "o":
                x, y = possitions[index_1][index_2][0], possitions[index_1][index_2][1]
                screen.blit(nought, (x, y))
    clock.tick()
    pygame.display.update()


draw_grid()
clock.tick()
pygame.display.update()
possitions = (
        ((0, 0, 348, 348), (366, 0, 714, 348), (732, 0, 1080, 348)),
        ((0, 366, 348, 714), (366, 366, 714, 714), (732, 366, 1080, 714)),
        ((0, 732, 348, 1080), (366, 732, 714, 1080), (732, 732, 1080, 1080))
    )
font = pygame.font.Font(None, 74)

for moves in range(9):
    if is_winner(main_board):
        time.sleep(1)
        screen.fill(WHITE)
        text_surface = font.render(f"{is_winner(main_board).upper()} wins!", True, BLACK)
        print(f"{is_winner(main_board).upper()} wins!")
        text_rect = text_surface.get_rect(center=(540, 540))
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        break


    if is_players_go():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for index_1, i_1 in enumerate(possitions):
                        for index_2, i_2 in enumerate(i_1):
                            x1, y1, x2, y2 = i_2[0], i_2[1], i_2[2], i_2[3]
                            if main_board[index_1][index_2] != " ":
                                pass
                            elif is_players_go() and ((mouse_x >= x1 and mouse_x <= x2) and (mouse_y >= y1 and mouse_y <= y2)):
                                main_board[index_1][index_2] = deepcopy(is_x_or_o())
                                draw_grid()
                                running = False
                                player_go += 1
    else:
        if num_of_spaces(main_board) == 9:
            board_thats_best = deepcopy(main_board)
            board_thats_best[0][0] = "x"
        else:
            best(main_board)
        main_board = deepcopy(board_thats_best)
        draw_grid()
        print("Computer made its move.")
        player_go += 1
    print_board()
if (is_winner(main_board) == None) and (num_of_spaces(main_board) == 0):
    time.sleep(1)
    screen.fill(WHITE)
    text_surface = font.render("It's a draw!", True, BLACK)
    print("It's a draw!")
    text_rect = text_surface.get_rect(center=(540, 540))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

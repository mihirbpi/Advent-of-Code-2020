from aocd import get_data
import copy

my_list = get_data(day=11).split("\n")
board = []

for i in range (0, len(my_list)):
    arr = list(my_list[i])
    board.append(arr)

def char_at(x, y, board):
    return board[y][x]

def is_occupied(x, y, board):
    return board[y][x] == "#"

def is_empty(x, y, board):
    return board[y][x] == "L"

def valid_pos(x, y, board):
    return (x >= 0 and x <= len(board[0]) - 1) and (y >= 0 and y <= len(board) - 1)

def neighbors(x, y, board):
    neighbors_list = []
    possible_neighbors = [ (x-1, y-1), (x,y-1), (x+1,y-1), (x-1, y), (x+1, y), (x-1, y+1), (x,y+1), (x+1,y+1) ]

    for pos in possible_neighbors:

        if(valid_pos(*pos, board)):
            neighbors_list.append(pos)

    return neighbors_list

def num_neighbors_occupied(x, y, board):
    occupied = 0

    for neighbor in neighbors(x, y, board):

        if(is_occupied(*neighbor, board)):
            occupied += 1

    return occupied

def num_occupied_total(board):
    count = 0

    for i in range (0, len(board)):

        for j in range(0, len(board[0])):

            if(board[i][j] == "#"):
                count += 1

    return count

def new_character(x, y, board):

    if(is_empty(x, y, board) and num_neighbors_occupied(x, y, board) == 0):
        return "#"

    elif(is_occupied(x, y, board) and num_neighbors_occupied(x, y, board) >= 4):
        return "L"

    else:
        return char_at(x, y, board)

def update_board(board):
    new_board = copy.deepcopy(board)

    for y in range(0, len(board)):

        for x in range(0, len(board[0])):
            new_board[y][x] = new_character(x, y, board)

    return new_board

def is_unchanged(board):

    if(update_board(board) != board):
                return False
    return True

while(not is_unchanged(board)):
    board = update_board(board)

print(num_occupied_total(board))

"""
Back tracking problems: Knight's Tour Problem
"""
import numpy as np


KNIGHT_MOVES = np.array([[1,2],[2,1], [-1,2],[-2,1], [-1,-2],[-2,-1], [1,-2],[2,-1]])


def get_valid_moves(current_position, current_board, moves = KNIGHT_MOVES):
    size_x,size_y = current_board.shape
    valid_moves = []
    for move in moves:
        new_position = current_position + move
        new_x, new_y = new_position
        if (new_x < size_x) and (new_y < size_y) and (new_x >= 0) and (new_y >= 0):
            if current_board[new_x,new_y] == 0:
                valid_moves.append(move)
    return np.array(valid_moves)


def knights_tour_step(current_position, current_board,current_depth):
    fill_target = current_board.shape[0]*current_board.shape[1]
    tour_complete = current_depth == fill_target
    if tour_complete:
        return True
    moves = get_valid_moves(current_position, current_board)
    if len(moves) == 0:
        return False
    for move in moves:
        new_position = current_position + move
        new_x, new_y = new_position
        new_depth = current_depth+1
        current_board[new_x,new_y] = new_depth
        tour_completed = knights_tour_step(new_position, current_board, new_depth)
        if tour_completed:
            return True
        current_board[new_x,new_y] = 0
    return False
        

def get_knights_tour(start_position = (0,0),board_size = (8,8)):
    board = np.zeros((board_size),dtype= np.uint8)
    board[start_position] = 1

    tour_status = knights_tour_step(start_position, board,1)
    return board


def main():
    board = get_knights_tour(board_size = (6,6))
    print(board)


if __name__ == '__main__':
    main()

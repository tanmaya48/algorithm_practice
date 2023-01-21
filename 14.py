#https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

import numpy as np

ATTACKED = 1
EMPTY = 0

def place_queen(position, board):
    position_x, position_y = position
    
    board[position_x,:] = ATTACKED
    board[:,position_y] = ATTACKED
    diagonal_directions = [[1,1],[-1,-1],[1,-1],[-1,1]]
    for direction in diagonal_directions:
        diag_dist = 1
        while True:
            try:
                move_x = direction[0]*diag_dist
                move_y = direction[1]*diag_dist
                new_x = position_x+move_x
                new_y = position_y+move_y
                if new_x*new_y > 0:
                    board[new_x,new_y]= ATTACKED
                    diag_dist+=1
                else:
                    break
            except:
                break
    return board
    

def get_valid_positions(board):
    valid_x,valid_y = np.where(board == EMPTY)
    valid_positions = [[x,y] for x,y in zip(valid_x,valid_y)]
    return valid_positions



def n_queens_step(board, N,queen_positions=[]):

    if len(queen_positions) == N:
        return True,queen_positions
    
    can_place_at = get_valid_positions(board)

    for position in can_place_at:
        new_board = board.copy()
        new_board = place_queen(position, new_board)
        placing_status,final_queens = n_queens_step(new_board, N,queen_positions= queen_positions + [position])
        if placing_status:
            return True,final_queens
        
    return False,[]



def get_n_queens(N = 8):
    board = np.zeros((N,N),dtype= np.uint8)
    status, queens = n_queens_step(board, N)
    if status:
        for queen in queens:
            x,y = queen
            board[x,y] = 1

        return board


def main():
    print(get_n_queens())


if __name__ == '__main__':
    main()

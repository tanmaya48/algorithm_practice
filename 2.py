#https://www.geeksforgeeks.org/min-cost-path-dp-6/
#this is the first attempt and not the optimal solution
from permutations import get_permutations
import random

direction_moves = {
            'down':[1,0],
            'right':[0,1],
            'diag':[1,1]
            }

def get_all_combinations(target):
    total_down , total_right = target
    total_diagonals = 0
    all_combinations = []

    while True:
        new_combination = ['diag' for i in range(total_diagonals)]+['down' for i in range(total_down)] + ['right' for i in range(total_right)]
        all_combinations.append(new_combination)
        if total_down * total_right == 0:
            break

        total_down-=1
        total_right-=1
        total_diagonals+=1

    return all_combinations




def get_all_paths(target):
    all_combinations = get_all_combinations(target)
    all_paths = []

    for combination in all_combinations:
        all_paths = all_paths + get_permutations(combination)

    return all_paths


def get_distance(moves,distance_matrix, pos_x = 0,pos_y=0):
    cummulative_weight = distance_matrix[pos_x][pos_y]   

    for move in moves:
        x,y = direction_moves[move]
        pos_x +=x
        pos_y +=y
        cummulative_weight+= distance_matrix[pos_x][pos_y]

    return cummulative_weight





def get_best_path(target,distance_matrix):
    all_paths = get_all_paths(target)
    prev_best_path = []
    prev_best_distance = 99999

    for path in all_paths:
        distance = get_distance(path, distance_matrix)
        if distance >prev_best_distance:
            continue
        prev_best_path = path
        prev_best_distance = distance
    
    return prev_best_path,prev_best_distance








def main():
    width,height = 6,6
    matrix = [[random.randint(1,10) for i in range(width)]for j in range(height)]
    for row in matrix:
        print(row)

    target = (5,5)

    print(get_best_path(target, matrix))
        



if __name__ == '__main__':

    main()


    
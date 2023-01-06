#https://www.geeksforgeeks.org/tile-stacking-problem/

from permutations import permutations_indexed


# m = tile sizes 1,2,3 ... m
# n = tower height
# k = number of copies of the same tile



def get_possible_stacks(n=3, m=3, k=2):
    # getting all tiles
    all_tiles = []
    for size in range(1,m+1):
        size_tiles = [size for i in range(k)]
        all_tiles  = all_tiles + size_tiles

    idx_permutations = permutations_indexed(N = len(all_tiles),R = n) # since n is the height of the tower
    permutations = [[all_tiles[idx] for idx in idx_perm] for idx_perm in idx_permutations]
    permutations = [sorted(perm) for perm in permutations]

    unique_permutations = [] 
    for perm in permutations:
        if perm in unique_permutations:
            continue
        unique_permutations.append(perm)


    return unique_permutations



def main():
    possible_stacks = get_possible_stacks()

    print(f'length: {len(possible_stacks)}')
    print(f'stacks: {possible_stacks}')

    

if __name__ == '__main__':
    main()
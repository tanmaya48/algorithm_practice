#https://www.geeksforgeeks.org/partition-problem-dp-18/

def get_superset(values):
    if len(values) == 1:
        return [[values[0]],[]]

    shorter_superset = get_superset(values[1:])
    new_sets = [ [values[0]]+shorter_set for shorter_set in shorter_superset]

    final_sets = shorter_superset + new_sets
    return final_sets


def is_partitionable(values):
    if sum(values)%2 != 0:
        return False
    
    half_sum = sum(values)/2
    all_subsets = get_superset(values)

    for subset in all_subsets:
        if sum(subset) == half_sum:
            return True

    return False





def main():
    values = [1, 3, 3, 2, 3, 2]
    print(is_partitionable(values))


if __name__ == '__main__':
    main()



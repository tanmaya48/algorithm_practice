#https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/

def remove_smaller(preceding, sequence):
    sequence_greater_than = []
    for value in sequence:
        if value>= preceding:
            sequence_greater_than.append(value)
    return sequence_greater_than


def max_sum_increasing_subsequence(sequence):

    if len(sequence) == 0:
        return 0
    if len(sequence) == 1:
        return sequence[0]
    
    sum_take = sequence[0]+max_sum_increasing_subsequence( remove_smaller(sequence[0],sequence[1:]) )
    sum_ignore = max_sum_increasing_subsequence( sequence[1:] )

    return max(sum_take,sum_ignore)



def main():
    sequence = [1, 101, 2, 3, 100, 4, 5]
    print(max_sum_increasing_subsequence(sequence))


if __name__ == '__main__':
    main()

#https://www.geeksforgeeks.org/longest-bitonic-subsequence-dp-15/

def remove_larger(preceding, sequence):
    sequence_greater_than = []
    for value in sequence:
        if value<= preceding:
            sequence_greater_than.append(value)
    return sequence_greater_than



def longest_descending(sequence):
    if len(sequence) <= 1:
        return sequence

    sequence_with = [sequence[0]] + longest_descending(remove_larger(sequence[0], sequence[1:]))
    sequence_without = longest_descending(sequence[1:])

    if len(sequence_with) >= len(sequence_without):
        return sequence_with
    return sequence_without
    


def longest_bitonic(sequence, previous = -99):
    if len(sequence) <= 1:
        return sequence

    down_path = longest_descending(remove_larger(previous, sequence))

    if sequence[0] < previous:
        bitonic_with = []
    else:
        bitonic_with = [sequence[0]] + longest_bitonic(sequence[1:],previous=sequence[0])
    bitonic_without = longest_bitonic(sequence[1:],previous=previous)

    if len(bitonic_with) > len(bitonic_without):
        bitonic = bitonic_with
    else:
        bitonic = bitonic_without

    if len(down_path)> len(bitonic):
        return down_path
    return bitonic



def main():
    sequence = [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]
    print(longest_bitonic(sequence))



if __name__ == '__main__':
    main()

    
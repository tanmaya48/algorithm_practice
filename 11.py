"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
since we pick 5 and 5.

Function signature: def largest_sum_of_nonadjacent_numbers(numbers: List[int]) -> int:
"""

def largest_sum_of_nonadjacent_numbers(numbers):
    if len(numbers) == 2:
        return max(numbers[0],numbers[1])
    if len(numbers) == 3:
        return max(numbers[0]+numbers[2],numbers[1])
    
    max_if_taken = numbers[0] + largest_sum_of_nonadjacent_numbers(numbers[2:])

    max_if_not_taken = largest_sum_of_nonadjacent_numbers(numbers[1:])

    return max(max_if_not_taken,max_if_taken)


def main():
    numbers = [2, 4, 6, 2, 5]
    print(largest_sum_of_nonadjacent_numbers(numbers))


if __name__ == '__main__':
    main()
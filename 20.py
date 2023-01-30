'''
 Countdown Numbers Game Solver
'''

def get_combination_pairs(numbers:list):
    pairs = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            pairs.append([numbers[i],numbers[j]])
    return pairs


def countdown_solver(numbers:list,target:int):
    if target in numbers:
        return True,[str(target)]
    combination_pairs = get_combination_pairs(numbers)
    
    for pair in combination_pairs:
        first,second = pair
        if first*second == 0:
            continue
        other_numbers = numbers.copy()
        other_numbers.remove(first)
        other_numbers.remove(second)
        #multiplication
        new_number = first*second
        found_target,steps = countdown_solver(other_numbers+[new_number], target)
        if found_target:
            return True, [f'{first}*{second}']+steps
        #addition
        new_number = first+second
        found_target,steps = countdown_solver(other_numbers+[new_number], target)
        if found_target:
            return True, [f'{first} +{second}']+steps
        #substraction
        new_number = first-second
        found_target,steps = countdown_solver(other_numbers+[new_number], target)
        if found_target:
            return True, [f'{first} - {second}']+steps
        #division
        if int(first/second) != first/second:
            continue
        new_number = first/second
        found_target,steps = countdown_solver(other_numbers+[new_number], target)
        if found_target:
            return True, [f'{first}/{second}']+steps
    return False,[]


def main():
    numbers = [2,9,9,25,100,50]
    target = 538
    print(numbers)
    print(target)
    found_target,steps = countdown_solver(numbers, target)
    print(steps)

if __name__ == '__main__':
    main()
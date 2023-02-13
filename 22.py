#Subset sum problem using backtracking

import random



def get_subset_with_sum(number_set,target_sum):
    if target_sum in number_set:
        return [target_sum]
    for i,number in enumerate(number_set):
        subtarget_sum = target_sum-number
        rest_of_set = [number_set[j] for j in range(len(number_set)) if j!=i]
        usable_subset = [num for num in rest_of_set if num <= subtarget_sum]
        
        result_subset = get_subset_with_sum(usable_subset,subtarget_sum)
        if result_subset is None:
            continue
        return [number]+ result_subset
    return None


def main():

    number_set =[random.randint(1,10) for i in range(10)]
    target_sum =random.randint(20,50)

    print(f'number_set: {number_set}')
    print(f'target_sum: {target_sum}')

    result = get_subset_with_sum(number_set,target_sum)
    print(result)
    

if __name__ == '__main__':
    main()

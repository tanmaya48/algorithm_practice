#https://www.geeksforgeeks.org/quick-sort/

import numpy as np

def quick_sort(unsorted_array: np.array):
    if len(unsorted_array) <= 1:
        return
    pivot_index = len(unsorted_array) -1
    pivot = int(unsorted_array[pivot_index])
    current_index = 0
    while current_index < len(unsorted_array):
        if unsorted_array[current_index] == unsorted_array[pivot_index]:
            current_index+=1
            continue
        if current_index < pivot_index:
            if unsorted_array[current_index] > unsorted_array[pivot_index]:
                unsorted_array[current_index],unsorted_array[pivot_index] = unsorted_array[pivot_index],unsorted_array[current_index]
                pivot_index = current_index
            current_index+=1
            continue
        #if current_index > pivot_index:
        if unsorted_array[current_index] < unsorted_array[pivot_index]:
            unsorted_array[current_index],unsorted_array[pivot_index] = unsorted_array[pivot_index],unsorted_array[current_index]
            pivot_index,current_index = current_index,pivot_index
            continue
        current_index+=1
    lower = unsorted_array[:pivot_index]
    upper = unsorted_array[pivot_index:]
    if len(lower) > 1:
        quick_sort(lower)
    if len(upper) > 1:
        quick_sort(upper)
    return



def main():
    unsorted_array = np.array([9,4,2,7,4,5,11,2,1,6,8,3])
    quick_sort(unsorted_array)
    print(unsorted_array)

if __name__ == '__main__':
    main()


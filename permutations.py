

def get_permutations(elements):

    permutations = []
    if len(elements) == 2:

        permutations.append([elements[0],elements[1]])
        permutations.append([elements[1],elements[0]])
        return permutations

    
    sub_permutations = get_permutations(elements[1:])
    
    to_add = elements[0]

    for sequence in sub_permutations:

        for i in range(len(elements)):

            new_permutation = sequence[:i] + [to_add] + sequence[i:]

            permutations.append(new_permutation)
    return permutations


def main():

    elements = ['a','a','a','d']

    permutations = get_permutations(elements)

    print(permutations)


if __name__ == '__main__':
    main()
    



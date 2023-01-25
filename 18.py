#https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/

def get_all_parenthesis(n_pairs):
    if n_pairs < 1:
        return []
    if n_pairs == 1:
        return ['{}']
    
    n_minus_one_parenthesis = get_all_parenthesis(n_pairs-1)
    n_parenthesis = []

    for parentheses in n_minus_one_parenthesis:
        n_parenthesis.append('{'+parentheses+'}')
        n_parenthesis.append('{}'+parentheses)
        n_parenthesis.append(parentheses+'{}')
    
    return list(set(n_parenthesis))


def main():
    n_pairs = 4
    print(get_all_parenthesis(n_pairs))


if __name__ == '__main__':
    main()
    
#https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sub_names = 'abcdefghijklmnopqrstuvwxyz'


def get_matrixes(chain):
    matrixes  = [(chain[i],chain[i+1]) for i in range(len(chain)-1)]

    matrix_dict = dict(zip(names,matrixes))
    return matrix_dict




def get_chain_cost(ordered_chain_string,matrix_dict):
    #ordered_chain_string= ordered_chain_string[1:-1]
    total_cost = 0
    dummy_dict = {}
    dummy_names = 'abcdefghijklmnopqrstuvwxyz'

    while True:
        closer = ordered_chain_string.find(')')
        if closer < 0:
            break
        
        half1,half2 = ordered_chain_string[:closer],ordered_chain_string[closer:]
        opener = ordered_chain_string[:closer].rfind('(')
        if opener < 0:
            break

        expression = half1[opener+1:]
        if len(expression) == 1:
            ordered_chain_string = half1[:opener] + half2[1:]
            continue

        term1,term2 = expression
        if term1 in matrix_dict.keys():
            size1 = matrix_dict[term1]
        else:
            size1 = dummy_dict[term1]
        if term2 in matrix_dict.keys():
            size2 = matrix_dict[term2]
        else:
            size2 = dummy_dict[term2]

        multiply_cost = size1[0] * size1[1] * size2[1]
        total_cost+=multiply_cost

        dummy_dict[dummy_names[0]] = (size1[0], size2[1])
        ordered_chain_string = half1[:opener]+dummy_names[0]+ half2[1:]
        dummy_names = dummy_names[1:]
        continue

    return total_cost
    



def get_all_chain_orders(chain_string):
    chain_orders = []
    if len(chain_string) < 2:
        return [chain_string]

    if len(chain_string) < 3:
        return [f'({chain_string})']
    
    for i in range(len(chain_string)-1):
        chain1 = chain_string[:i+1]
        chain2 = chain_string[i+1:]

        chain_1_paths = get_all_chain_orders(chain1)
        chain_2_paths = get_all_chain_orders(chain2)

        for c1_path in chain_1_paths:
            for c2_path in chain_2_paths:
                chain_orders.append("("+c1_path+c2_path+")")
    
    return chain_orders




def get_best_chain(chain):

    matrix_dict = get_matrixes(chain)

    chain_string = ''.join(matrix_dict.keys())
    print(chain_string)
    chain_orders = get_all_chain_orders(chain_string)
    
    min_cost = get_chain_cost(chain_orders[0], matrix_dict)
    best_chain = chain_orders[0]

    for order_string in chain_orders:
        cost = get_chain_cost(order_string, matrix_dict)
        
        if cost < min_cost:
            min_cost= cost
            best_chain = order_string
    
    return min_cost,best_chain




def main():
    chain = [10, 30, 5, 60]
    min_cost,best_chain = get_best_chain(chain)
    print(f'best cost: {min_cost}')
    print(f'best matrix chain: {best_chain}')





if __name__ == '__main__':
    main()

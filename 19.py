'''
get all bracket combinations in a math expression
for example:
INPUT :1+2x3
OUTPUT: (1+(2x3)),((1+2)x3)

INPUT :1+2
OUTPUT: (1+2)

INPUT: 1+2x3/4
OUTPUT: ((1+(2x3))/4), (((1+2)x3)/4), ((1+2)x(3/4)), (1+(2x(3/4))), (1+((2x3)/4))
'''

import re

SYMBOLS = '-|\+|x|/|'


def string_to_sets(expression):
    numbers = re.split(SYMBOLS, expression)
    numbers = [num for num in numbers if num != '' ]

    symbols = re.split('|'.join(numbers), expression)
    symbols = [sym for sym in symbols if sym != '' ]

    return numbers,symbols


def put_brackets(numbers,symbols):
    assert len(numbers) == len(symbols) + 1
    if len(numbers) == 1:
        return numbers
    if len(numbers) == 2:
        return ['('+numbers[0] + symbols[0] + numbers[1]+')']
    
    all_combinations = []
    for idx in range(len(symbols)):
        symbol = symbols[idx]
        
        pre_numbers = numbers[:idx+1]
        post_numbers = numbers[idx+1:]

        pre_symbols = symbols[:idx]
        post_symbols = symbols[idx+1:]

        pre_combinations = put_brackets(pre_numbers, pre_symbols)
        post_combinations = put_brackets(post_numbers, post_symbols)

        for pre_combo in pre_combinations:
            for post_combo in post_combinations:
                combination = '('+ pre_combo + symbol + post_combo +')'
                all_combinations.append(combination)
    return all_combinations



def get_all_brackets(expression):
    numbers,symbols = string_to_sets(expression)
    return put_brackets(numbers, symbols)


def main():
    expression = '1+2x3/4'
    print(get_all_brackets(expression))

if __name__ == '__main__':
    main()
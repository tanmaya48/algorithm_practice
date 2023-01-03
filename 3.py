#https://www.geeksforgeeks.org/coin-change-dp-7/



def get_coin_combinations(coin_types, target_sum):
    combinations = []
    
    for coin in coin_types:
        if coin == target_sum:
            combinations.append([coin])
        if coin > target_sum:
            continue
        sub_combinations = get_coin_combinations(coin_types, target_sum - coin)

        new_combinations = [[coin]+ sub_combo for sub_combo in sub_combinations]

        combinations = combinations + new_combinations

    return combinations


def main():

    coin_types = [1,2,5]
    target_sum = 11

    combinations = get_coin_combinations(coin_types, target_sum)
    combinations = set(tuple(sorted(combo)) for combo in combinations)
    print(combinations)


if __name__ == '__main__':
    main()
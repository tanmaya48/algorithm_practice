#https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/


def is_palindrome(word):
    return word[::-1] ==word



def get_palindrome_partition(word):
    if len(word) == 0:
        return []
    if is_palindrome(word):
        return [word]

    if len(word)==2:
        return [word[0],word[1]]

    best_partitioning = [char for char in word]

    for word_end in range(len(word)):
        current_partition = word[:word_end+1]
        if not is_palindrome(current_partition):
            continue

        rest_of_the_word = word[word_end+1:]

        partitioning = [current_partition] + get_palindrome_partition(rest_of_the_word)

        if len(partitioning) < len(best_partitioning):
            best_partitioning = partitioning

    return best_partitioning





def main():
    words = ['geek','ababbbabbababa','abcde']
    for word in words:
        print(get_palindrome_partition(word))



if __name__ == '__main__':
    main()
    
#https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/






def longest_palindrome_subsequence(word):
    if len(word) == 1:
        return 1
    if len(word) == 2:
        if word[0] == word[-1]:
            return 2
    
    if word[0] == word[-1]:
        return 2 + longest_palindrome_subsequence(word[1:-1])

    return max( [longest_palindrome_subsequence(word[:-1]),longest_palindrome_subsequence(word[1:]) ])




def main():
    word = 'geeksforgeeks'
    print(longest_palindrome_subsequence(word))


if __name__ == "__main__":
    main()
    

#https://www.geeksforgeeks.org/edit-distance-dp-5/


def get_edit_distance(word1,word2):

    if len(word1)> len(word2):
        word1,word2 = word2,word1


    edits = 0

    num_chars_to_remove = len(word2) - len(word1)

    curr_char = 0

    new_word = ''

    while word1 != new_word:
        
        #character matches
        if word2[0] == word1[curr_char]:
            new_word = new_word + word2[0]
            curr_char += 1
            word2 = word2[1:]
            continue
        
        #remove extra character
        if num_chars_to_remove > 0:
            word2 = word2[1:]
            edits+=1
            num_chars_to_remove-=1
            continue
        
        #replace character
        new_word = new_word + word1[curr_char]
        curr_char += 1
        word2 = word2[1:]
        edits+=1

    return edits


if __name__ == '__main__':

    d = get_edit_distance('sunday', 'wednesday')
    print(d)

    









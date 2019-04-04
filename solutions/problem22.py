# note: assumes that the input string and the dictionary/set of strings all use 
# lowercase strings
def reconstruct_sentence(words: set, sentence: str):

    curr_word = ''
    reconstructed_sentence = []

    for i in range(len(sentence)):
        curr_word += sentence[i]

        if curr_word in words:
            reconstructed_sentence.append(curr_word)
            curr_word = ''

    return reconstructed_sentence if len(reconstructed_sentence) > 0 else None

# could also use dictionaries here (as the problem states), but sets are more suited
# since there isn't a value
test1 = (set(['quick', 'brown', 'the', 'fox']), 'thequickbrownfox')
test2 = (set(['bed', 'bath', 'bedbath', 'and', 'beyond']), 'bedbathandbeyond')
test3 = (set(['i', 'am', 'the', 'one', 'who', 'knocks', 'at', 'door']), 'iamtheonewhoknocksatthedoor')

print(reconstruct_sentence(*test1))     # expected out: ['the', 'quick', 'brown', 'fox']
print(reconstruct_sentence(*test2))     # expected out: ['bed', 'bath', 'and', 'beyond'] or ['bedbath', 'and', 'beyond']
print(reconstruct_sentence(*test3))     # expected out: ['i', 'am', 'the', 'one', 'who', 'knocks', 'at', 'the', door']
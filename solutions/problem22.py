def reconstruct_sentence(words: set, sentence: str):

    curr_word = ''
    reconstructed_sentence = []

    for i in range(len(sentence)):
        curr_word += sentence[i]

        if curr_word in words:
            reconstructed_sentence.append(curr_word)
            curr_word = ''

    return reconstructed_sentence

test1 = (set(['quick', 'brown', 'the', 'fox']), 'thequickbrownfox')
test2 = (set(['bed', 'bath', 'and', 'beyond']), 'bedbathandbeyond')

print(reconstruct_sentence(*test1))
print(reconstruct_sentence(*test2))
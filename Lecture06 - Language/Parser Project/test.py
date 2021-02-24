import nltk

def test(sentence):
    tokenized_string = nltk.word_tokenize(sentence)
    word_list = []

    for i, word in enumerate(tokenized_string):
        for letter in word:
            if letter.isalpha():
                word_list.append(word.lower())
                break
        print(i)
    
    return word_list

print(test('LINDA 20GOSTOSA'))
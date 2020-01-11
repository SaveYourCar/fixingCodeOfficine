def pig_latin(sentence):
    sentence_words=sentence.split()
    pig_sentence=""
    for word in sentence_words:
        pig_sentence_word=word[1:]+word[0]+"ay"
        pig_sentence+=pig_sentence_word+" "
    pig_sentence=pig_sentence[:-1]
    return pig_sentence

print(pig_latin(input()))
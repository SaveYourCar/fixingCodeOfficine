import string
import re


def revers_alphabet_string(phrase):
    alphabet = string.ascii_lowercase
    reverse_alphabet = alphabet[::-1]
    reverse_phrase=""
    for i in phrase.lower():
        if not re.match(r"[A-Za-z]",i):
            reverse_phrase += i
        else:
            index = alphabet.index(i) 
            reverse_phrase += reverse_alphabet[index]
    return reverse_phrase

print(revers_alphabet_string(input()))




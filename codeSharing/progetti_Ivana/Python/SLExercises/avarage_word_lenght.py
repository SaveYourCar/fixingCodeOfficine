import math
import re

def avg_word_lenght(some_text):
    words=re.findall(r"([A-Za-z]+)", some_text)
    avarage=math.ceil(sum(map(len, words))/len(words))
    return avarage
print(avg_word_lenght(input()))

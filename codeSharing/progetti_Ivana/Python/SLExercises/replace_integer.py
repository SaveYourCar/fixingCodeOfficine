import re

numbers= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def find_numbers(phrase):
    string_numbers =  re.findall(r"(10|\d)", phrase)
    for number in string_numbers:
        phrase = phrase.replace(number, numbers[int(number)])
    return phrase

print(find_numbers(input()))
   
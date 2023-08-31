import random

def generate_anagram(input_str):
    char_list = list(input_str)
    
    random.shuffle(char_list)
    
   
    anagram = ''.join(char_list)
    
    return anagram


input_word = input("Enter a word or phrase: ")


anagram = generate_anagram(input_word)
print("Anagram:", anagram)

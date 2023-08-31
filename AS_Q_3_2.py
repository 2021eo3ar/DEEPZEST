# from itertools import permutations

# def generate_anagrams(input_str):
#     input_str = input_str.replace(" ", "").lower()
#     unique_anagrams = set()
    
#     for perm in permutations(input_str):
#         anagram = ''.join(perm)
#         unique_anagrams.add(anagram)
    
#     return unique_anagrams

# def main():
#     input_word = input("Enter a word or phrase: ")
#     anagrams = generate_anagrams(input_word)
    
#     if len(anagrams) > 1:
#         anagrams.discard(input_word.lower())
#         print("Anagrams of '{}': {}".format(input_word, ', '.join(anagrams)))
#     else:
#         print("No anagrams found for '{}'.", input_word)

# if __name__ == "__main__":
#     main()

# def is_anagram(word1, word2):
#     return sorted(word1) == sorted(word2)

# def find_anagrams(word, word_list):
#     anagrams = []
#     for w in word_list:
#         if is_anagram(word, w):
#             anagrams.append(w)
#     return anagrams

# def main():
#     input_word = input("Enter a word: ").lower()
#     input_list = input("Enter a list of words, separated by spaces: ").lower().split()
    
#     anagrams = find_anagrams(input_word, input_list)
    
#     if anagrams:
#         print("Anagrams of '{}': {}".format(input_word, anagrams))
#     else:
#         print("No anagrams found for '{}'.", input_word)

# if __name__ == "__main__":
#     main()

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def find_anagrams(word, word_list):
    anagrams = []
    for w in word_list:
        if is_anagram(word, w):
            anagrams.append(w)
    return anagrams

def main():
    input_word = input("Enter a word: ").lower()
    input_list = input("Enter a list of words, separated by spaces: ").lower().split()
    
    anagrams = find_anagrams(input_word, input_list)
    
    if anagrams:
        print("Anagrams of '{}': {}".format(input_word, anagrams))
    else:
        print("No anagrams found for '{}'.", input_word)

if __name__ == "__main__":
    main()

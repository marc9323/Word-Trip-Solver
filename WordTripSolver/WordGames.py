
"""
This program will help WordTrip players to cheat.  User will enter the multiple characters [a-Z] and
return all possible combinations of the letters that form words.  The application will contain a large
dictionary against which possible combinations will be checked.

I will use a brute force algorithm initially which will return every possible combination of characters
formed by the character cluster.  Certain constraints must be instituted such that words of a certain
length, for example, a single character 'I', or two characters like 'to', will be set aside into a
'bonus bin'.

A sample run might look like this:

Enter the character cloud to create words from:
user: H O P E

An algorithm will check every possible combination of letters for matches in the dictionary.
If there is no match - is not a word.

A list of possible words is then given the user.

Also there should be opportunity to set constraints - such as
all possible qualifying words must be of such and such length.
"""


#  This is a good stack overflow question
from itertools import permutations

ALL_WORDS = []

def get_user_input():
    char_set = input('Please enter the desired character set:  (i.e. hope  ')
    resultant_word_length = int(input("Enter the size of word(s) you are looking for: "))
    return char_set, resultant_word_length


# def get_permutations(char_set):
#    return ([''.join(p) for p in permutations(char_set)])


def load_dictionary(filename):
    with open('corncob_lowercase.txt', 'r') as file:
        for line in file:
            for word in line.split():
                ALL_WORDS.append(word)
        return ALL_WORDS


def get_good_words(possible_permutations):
    good_words = []
    #  optimize this
    for word in ALL_WORDS:
        for combination in possible_permutations:
            if word == combination:
                good_words.append(word)

    return good_words

# def check_words(possible_permutations):
#     checked_words = any(ALL_WORDS)
#     return checked_words


# def get_possible_permutations(character_string, length):
#     return [''.join(p) for p in permutations(character_string, length)]


def main():
    #  load the dictionary into memory
    ALL_WORDS = load_dictionary('corncob_lowercase.txt')

    #  get character string fronm the user
    character_string, result_length = get_user_input()

    #  get list of all possible permutations of the chaparacter_string

    #  problem - this gives us the possible permutations for hope
    #  len(character_string)
    #  but we want all possible lengths
    for i in range(1, result_length):
        possible_permutations = ([''.join(p) for p in permutations(character_string, i)])

    print("Possible X Letter Permutations: ")
    print(possible_permutations)
    print("Matching words: ")

    good_words = get_good_words(possible_permutations)
    #  take care to append the initial permutation
    if ALL_WORDS.count(character_string) == 1:
        #  if the permutation is present in dictionary ALL_WORDS
        #  then append it to the list of good words
        good_words.append(character_string)
    print(good_words)

#  REMEMBER THE OFF BY 1 ERROR FOR PYTHON LIST STARTING AT XERO

main()



# def permutations(string, step=0):
#     if step == len(string):
#         #  we've reached the end, print permutation
#         print("".join(string))
#     for i in range(step, len(string)):
#         #  copy the string (store as array)
#         string_copy = [c for c in string]
#         #  swap the current index with the step
#         string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
#         #  recurse on the portion of the string that has not been swapped yet
#         permutations(string_copy, step + 1)
#
# all_words = load_dictionary('corncob_lowercase.txt')
#
# print(all_words)


# 1.  Method to generate and return set of all possible permutations of the given set.

# 2.  Check each permutation against corncob.

# 3.  If permutation is in list, add to set of possible words.

# good_words = []
#     for word in ALL_WORDS:
#         for combination in possible_permutations:
#             if word == combination:
#                 good_words.append(combination)

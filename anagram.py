"""
File: anagram.py
Name: Yudy
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dictionary = []               # The dictionary imported.
anagram = []                      # The result of anagrams.


def main():
    global anagram
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        typing = input('Find anagrams for: ')
        if typing == EXIT:
            break
        print('Searching...')
        find_anagrams(typing)
        print(f'{len(anagram)} anagrams: {anagram}')
        anagram.clear()


def read_dictionary():
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            words = line.split()
            dictionary.append(words[0])
    return dictionary


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    current = ''
    find_anagrams_helper(s, current, len(s))


def find_anagrams_helper(word, current_index, length):
    """
    :param word:
    :param current_index:
    :param length:
    :return:
    """
    global anagram
    # Base case.
    if len(current_index) == length:
        # To get the alpha of index.
        current_word = ''
        for i in range(length):
            current_word += word[int(current_index[i])]
        if current_word in dictionary:
            if current_word not in anagram:
                anagram.append(current_word)

                print(f'Found: {current_word}')
                print('Searching...')

    # Recursive case.
    else:
        if has_prefix(current_index, word):
            for j in range(length):
                # Avoid same alpha.
                if str(j) not in current_index:
                    current_index += str(j)                                 # Choose.
                    find_anagrams_helper(word, current_index, length)       # Explore.
                    current_index = current_index[:len(current_index) - 1]  # Un-choose.


def has_prefix(sub_index, word):
    """
    :param sub_index:
    :param word
    :return:
    """
    global dictionary
    current_word = ''
    for i in range(len(sub_index)):
        current_word += word[int(sub_index[i])]
    for word in dictionary:
        if word.startswith(current_word):
            return True

    return False


def test():
    s = 'apple'
    print(s[1:len(s)])


if __name__ == '__main__':
    main()

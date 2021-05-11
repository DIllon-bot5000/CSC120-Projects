"""
    File: rhymes.py
    Author: Dillon Barr
    Purpose: Finds the perfect rhymes of a user input word that exist in a given text file.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""

def main():
    word_dict = {}
    open_files(word_dict)
    user_word, user_pronunciation = get_user_input(word_dict)
    find_stress_vowel(user_word, user_pronunciation, word_dict)
    
def open_files(word_dict):
    """ 
    Opens a text file and stores the contents into a dictionary with
    the word as the key and the pronunciations as the values broken up into
    lists of lists.
  
    Parameters: word_dict is an empty dictionary to be filled.
  
    Returns: A dictionary filled with words and their pronunciations.
    """
    user_file = input()
    file = open(user_file)
    for line in file:
        empty_list = []
        line = line.strip().split()
        key = line[0]
        pronunciation_list = (line[1:])
        empty_list.append(pronunciation_list)
        if key in word_dict:
            word_dict[key].append(pronunciation_list)
        else:
            word_dict[key] = empty_list
    return word_dict

def get_user_input(word_dict):
    """ 
    Gets the user input of a string and finds all the pronunciations
    associated with that word.
  
    Parameters: word_dict is a dictionary filled with words and their pronunciations.
  
    Returns: The word taken from input as well as the found pronunciations.
    """
    word = input().upper()
    if word in word_dict:
        pronunciation = word_dict[word]
    return word, pronunciation

def find_stress_vowel(word, pronunciation, dictionary):
    """ 
    Finds the primary stress vowel in the pronunciations associated with the 
    given word. It then calls another function to find and print all the perfect rhymes.
  
    Parameters: word is the user input string 
                
                pronunciation is the list of lists containing 
                the phonemes of that word
                
                dictionary is collection of words and 
                pronunciations read in from the text file.
  
    Returns: None
    """
    for elements in pronunciation:
        for j in range(len(elements)):
            if '1' in elements[j]:
                stress_vowel = elements[j]
                stress_index = j
                find_rhymes(word, elements, dictionary, stress_vowel, stress_index)

def find_rhymes(word, element, dictionary, stress, stress_index):
    """ 
    This function searches though the dictionary of words and pronunciations. When
    the key doesn't equal the user word it then loops through the pronunciations of the
    key and checks if the pronunciations qualify the word as a perfect rhyme and prints out the
    words that are rhymes.
  
    Parameters: word is the user input string 
                
                element is the specific pronunciation of the word
                being searched in the find_stress_vowell function
                
                dictionary is collection of words and 
                pronunciations read in from the text file.
                
                stress is a string representing the primary stress vowel in
                the current pronunciation of the word.
                
                stress index is the index of the vowel found in the elements list.
  
    Returns: None.
    """
    
    for words, pronunciations in dictionary.items():
        counter = 0
        for list in pronunciations:
            for syllable in range(len(list)):
                placeholder_index = 0                    
                if list[syllable] == stress:
                    placeholder_index = syllable
                    if placeholder_index and stress_index == 0:
                        continue
                    if placeholder_index == 0 and pronunciations[counter][placeholder_index +1:] == \
                    element[stress_index +1:]:
                        print(words)
                    elif pronunciations[counter][placeholder_index +1:] == element[stress_index +1:] and \
                    element[stress_index -1] != pronunciations[counter][placeholder_index - 1]:
                        print(words)
            counter += 1
            
    
main()
        
        
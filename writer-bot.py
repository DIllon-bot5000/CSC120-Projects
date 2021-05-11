"""
    File: writer-bot.py
    Author: Dillon Barr
    Purpose: Reads in a text file and after getting the user's desired output length
             generates a new text comprised of the original in a random order using
             a Markov table.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""

import random
NONWORD = " "
SEED = 8


def main():
    random.seed(SEED)
    input_list = []
    markov_dict = {}
    file_name, prefix_size, text_size = get_input()
    input_list = open_file(file_name)
    markov_dict = create_dictionary(input_list, prefix_size)
    create_text(input_list, prefix_size, markov_dict, text_size,)

def get_input():
    """ 
    Reads in the user input for the name of the text file, the length of the
    prefixes in the table, and the desired length of the output text. These variables
    are returned to main.
  
    Parameters: none
  
    Returns: A string, and two integers.
    """
    file_name = input()
    prefix_size = int(input())
    assert prefix_size >= 1
    text_size = int(input())
    assert text_size >= 1
    return file_name, prefix_size, text_size

def open_file(file_name):
    """ 
    Takes the file name the user previously input and stores each word as an
    element of a single dimension list.
  
    Parameters: file_name is a sting associated with the text file the user input.
  
    Returns: A list filled with the contents of the text file.
    """
    input_list = []
    file = open(file_name)
    for line in file:
        line = line.strip().split()
        input_list += line
    return input_list
     
def create_dictionary(text_list, prefix):
    """ 
    Creates a dictionary populated with prefixes as keys and suffixes as the values. This
    function calls two other functions in order to create the tuple prefixes and then loops through
    the text_list to find possible suffixes for all prefixes.
  
    Parameters: text_list is the list filled with the elements of the original text
                and prefix is an integer representing the user input desired prefix size.
  
    Returns: A dictionary filled with the possible prefixes as the keys
             and possible suffixes as the values.
    """
    word_dict = {}
    key = make_tuple(NONWORD, prefix)
    for item in range(len(text_list)):
        if key in word_dict:
            word_dict[key].append(text_list[item])
        else:
            word_dict[key] = [text_list[item]]
        key = shift_tuple(key, text_list[item])
    return word_dict
        
def make_tuple(item, n):
    """ 
    Creates a tuple consisting of an element item n times in a tuple.
  
    Parameters: item is the element used to popualte the tuple and n is the
                number of items in the tuple.
  
    Returns: A tuple
    """
    new_tuple = []
    for elements in range(0, n):
        new_tuple.append(item)
    return tuple(new_tuple)

def shift_tuple(tup, value):
    """ 
    Takes a tuple and a value to be added to the tuple and shifts the contents
    of the tuple to remove the first element and add the value to the end
    of the tuple.
  
    Parameters: tup is the orginal tuple being shifted and value is the variable being
                added to the end of the tuple.
  
    Returns: A tuple.
    """
    holder = []
    for i in range(1, len(tup)):
        holder.append(tup[i])
    holder.append(value)
    return tuple(holder)

def create_prefix(text, prefix):
    """ 
    Opens a text file and stores the contents into a dictionary with
    the word as the key and the pronunciations as the values broken up into
    lists of lists.
  
    Parameters: text is the list of the original file contents and prefix
                is an integer containing the desired length of the prefix.
  
    Returns: A tuple
    """
    holder = []
    for items in text[:prefix]:
        holder.append(items)
    holder = tuple(holder)
    return holder
        
def create_text(text_list, prefix_size, dictionary, text_size):
    """ 
    Creates a new list containing the randomly generated text from the original. This function creates
    the intial prefix of the first few elements of the original file and then loops as many times as the 
    text_size wants. While looping, if the prefix exists in the dictionary a random suffix is selected,
    appended to the new text, and shifted into the prefix tuple.
  
    Parameters: text_list is the list of the original text from the file.
                prefix_size is the user input integer denoting the desired prefix size.
                dictionary is the markov table containing prefixes as keys and suffixes as values.
                text_size is an integer denoting the desired length of the output text.
  
    Returns: None.
    """
    new_text = []
    new_word = ''
    for item in text_list[:prefix_size]:
        new_text.append(item)
    prefix = create_prefix(text_list, prefix_size)
    for text in range(0, text_size + 1):
        if prefix in dictionary:
            if len(dictionary[prefix]) > 1:
                new_word = dictionary[prefix][random.randint(0, len(dictionary[prefix]) - 1)]
            else:
                new_word = dictionary[prefix][0]
        new_text.append(new_word)
        prefix = shift_tuple(prefix, new_word)
    print_text(new_text, text_size)

def print_text(text, text_size):
    """ 
    Takes the list of random text and prints it out 10 words per line until it reaches the 
    desired output length or there are less than 10 words left and then it prints the remainder.
  
    Parameters: text is the list of randomly selected words from original text.
                text_size is the user denoted desired output length.
  
    Returns: None
    """
    counter = text_size
    for words in range(0, text_size, 10):
        if counter >= 10:
            print(' '.join(text[words: words + 10]))
        else:
            print(' '.join(text[words: words + counter]))
        counter -= 10
main()
            
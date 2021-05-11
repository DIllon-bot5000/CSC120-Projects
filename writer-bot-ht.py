'''
Created on Apr 28, 2019

@author: dbarr
'''
import random
SEED = 8
NONWORD = '@'

class Hashtable:
    def __init__(self, size):
        self._pairs = [None] * size
        self._size = size
    def put(self, key, value):
        i = self._hash(key)
        while self._pairs[i] != None:
            i -= 1
            if i < 0:
                i = len(self._pairs) - 1
        self._pairs[i] = [key, value]
    def get(self, key):
        i = self._hash(key)
        while self._pairs[i] != None:
            if self._pairs[i][0] == key:
                return self._pairs[i][1]
            i -= 1
            if i<0:
                i = len(self._pairs) - 1
        return None
    def add(self, key, value):
        i = self._hash(key)
        while self._pairs[i][0] != key:
            i -= 1
            if i < 0:
                i = len(self._pairs) - 1
        self._pairs[i][1].append(value)
    def _hash(self, key):
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size
    def __contains__(self, key):
        i = self._hash(key)
        while self._pairs[i] != None:
            if self._pairs[i][0] == key:
                return True
            i -= 1
            if i<0:
                i = len(self._pairs) - 1
        return False
    def __str__(self):
        pass
    def print_all(self):
        for i in range(self._size):
            if self._pairs[i] != None:
                pair = self._pairs[i]
                print("{} : {}/{}".format(i, pair[0], pair[1]))
def main():
    random.seed(SEED)
    file_name = input()
    hash_size = int(input())
    prefix_size = int(input())
    word_count = int(input())
    hashTable = Hashtable(hash_size)
    input_list = open_file(file_name)
    if prefix_size >= 1 and word_count >= 1:
        populate_hashTable(prefix_size, input_list, hashTable, word_count)
    elif prefix_size < 1:
        print('ERROR: specified prefix size is less than one')
    elif word_count < 1:
        print('ERROR: specified size of the generated text is less than one')
    
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

def populate_hashTable(prefix, text_list, table, word_count):
    """ 
    Populates a Hashtable object with the keys and values generated from the input text. Calls
    a function to create the random text after.
  
    Parameters: prefix is the prefix size, text_list is the input file as a list, table is the
                Hashtable object and word_count is the desired output length.
    
    Precondition: valid input has been read in and a Hashtable has been initialized.
    
    Postcondition: the Hashtable object has been populated with keys and values.
  
    Returns: None
    """
    key = make_tuple(NONWORD, prefix)
    for item in range(len(text_list)):
        if key in table:
            table.add(key, text_list[item])
        else:
            table.put(key, [text_list[item]])
        key = shift_tuple(key, text_list[item])
    create_text(text_list, prefix, word_count, table)
def create_prefix(text, prefix):
    """ 
    Creates an inital prefix using the first indexes of the original text list
    to reach the prefix length.
  
    Parameters: text is the list of the original file contents and prefix
                is an integer containing the desired length of the prefix.
    
    Precondition: valid input has been read in from the user.
    
    Postcondition: a string has been created to be a prefix.
  
    Returns: A string
    """
    holder = []
    for items in text[:prefix]:
        holder.append(items)
    return ' '.join(holder)

def shift_tuple(tup, value):
    """ 
    Takes a string and a value to be added to the string and shifts the contents
    of the string to remove the first element and add the value to the end
    of the string.
  
    Parameters: tup is a string needing to be shifted and value is the string needing to
                be added to tup.
                
    Precondition: valid input has been read in
    
    Postcondition: a string used as a prefix has been modified.
  
    Returns: A string
    """
    tup = tup.strip().split()
    holder = []
    for i in range(1, len(tup)):
        holder.append(tup[i])
    holder.append(value)
    return ' '.join(holder)
def make_tuple(item, n):
    """ 
    Creates a string consisting of an element item n times in a string.
  
    Parameters: item is the element used to populate the string and n is the
                number of items in the string.
                
    Precondition: valid input has been read in.
    
    Postcondition: an initial prefix has been created.
  
    Returns: A string
    """
    new_tuple = []
    for elements in range(0, n):
        new_tuple.append(item)
    return ' '.join(new_tuple)

def create_text(text_list, prefix_size, text_size, table):
    """ 
    Creates a new list containing the randomly generated text from the original. This function creates
    the intial prefix of the first few elements of the original file and then loops as many times as the 
    text_size wants. While looping, if the prefix exists in the hashtable a random suffix is selected,
    appended to the new text, and shifted into the prefix tuple.
  
    Parameters: text_list is the list of the original text from the file.
                prefix_size is the user input integer denoting the desired prefix size.
                table is the Hashtable containing prefixes as keys and suffixes as values.
                text_size is an integer denoting the desired length of the output text.
    
    Precondition: Valid input read in and a table populated with keys and values. 
    
    Postcondition: Random text based on the original is generated.
    
    Returns: None.
    """
    new_text = []
    new_word = ''
    for item in text_list[:prefix_size]:
        new_text.append(item)
    prefix = create_prefix(text_list, prefix_size)
    for text in range(0, text_size+1):
        value = table.get(prefix)
        if len(value) > 1:
            new_word = value[random.randint(0, len(value) - 1)]           
        else:
            new_word = value[0]
        new_text.append(new_word)
        prefix = shift_tuple(prefix, new_word)
    print_text(new_text, text_size)
def print_text(text, text_size):
    """ 
    Takes the list of random text and prints it out 10 words per line until it reaches the 
    desired output length or there are less than 10 words left and then it prints the remainder.
  
    Parameters: text is the list of randomly selected words from original text.
                text_size is the user denoted desired output length.
                
    Precondition: valid input read in, table populated and random text generated from original
    
    Postcondition: The random text is printed out 10 per line.
  
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
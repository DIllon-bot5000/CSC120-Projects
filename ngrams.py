"""
    File: ngrams.py
    Author: Dillon Barr
    Purpose: Scans a text file and prints out the strings that occur most along with the
             number of occurrences.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""

import sys
class Input:
    '''
    This class takes a file to be opened from user input
    and opens it.
    '''
    def __init__(self):
        '''
        Gets the users input and opens the file.
         
        Parameters: None
        
        Pre-condition: The Input class has been called.
        
        Post-condition: The user file is opened.
                    
        Returns: None
        '''
        try:
            self._input = input()
            self._file = open(self._input)
        except IOError:
            print("ERROR: Could not open file " + self._input)
            sys.exit(1)
    def wordlist(self):
        '''
        Loops through the opened file and reads in the text. Strips out spaces and
        leading and trailing punctuation. Makes each word lowercase and appends it to 
        the word_list.
         
        Parameters: none
        
        Pre-condition: the file has been opened in __init__
        
        Post-condition: word_list is now filled with contents from the file.
                    
        Returns: a list filled with words from the file.
        '''
        word_list = []
        for line in self._file:
            assert len(line) > 0, 'Empty file'
            line = line.strip().split()
            for item in line:
                item = item.strip('-".,?!:;$').strip()
                item = item.strip("'")
                word_list.append(item.lower())
        while "" in word_list:
            word_list.remove("")
        return word_list
    
class Ngrams:
    def __init__(self):
        '''
        Gets an integer input from the user which will be the ngram length.
        Creates a dictionary to store the strings and their total occurrences.
         
        Parameters: none
        
        Pre-condition: A Ngrams object has been created in main.
        
        Post-condition: ngram length is established and a dictioanry is created.
                    
        Returns: none.
        '''
        new_input = int(input())
        assert new_input > 0, 'Invalid ngram length input.'
        self._length = new_input
        self._ngram_dict = {}
    def update(self, ngram):
        '''
        Takes a string and checks if a key made up of this string exists and 
        increments the occurrence if so. Otherwise a key is created and initial occurrence 
        counted.
         
        Parameters: ngram is a string.
        
        Pre-condition: an ngram variable has been created.
        
        Post-condition: a key has been created and its value incremented or an
                        existing value is updated.
                    
        Returns: none
        '''
        if ngram not in self._ngram_dict:
            self._ngram_dict[ngram] = 0
        self._ngram_dict[ngram] += 1
    def process_wordlist(self, wordlist):
        '''
        Loops through the wordlist and creates each variation of ngram and sends
        it to the update method.
         
        Parameters: wordlist is the list of text created in the Input class.
        
        Pre-condition: An Input object has been created and a valid wordlist exists.
        
        Post-condition: the dictionary of strings and occurrences is updated.
                    
        Returns: none
        '''
        assert self._length <= len(wordlist), 'Ngram length longer than word list.'
        for index in range(len(wordlist)):
            if index + self._length > len(wordlist):
                break
            else:
                ngram = str(' '.join(wordlist[index:index+self._length]))
                self.update(ngram)
    def print_max_ngrams(self):
        '''
        Establishes the most occurrences of a string in the dictionary and
        prints out the string and how many times it's found.
         
        Parameters: none are passed in.
        
        Pre-condition: The self._ngram_dict is populated.
        
        Post-condition: The max is found and output.
                    
        Returns: none.
        '''
        highest = max(self._ngram_dict.values())
        for k, v in self._ngram_dict.items():
            if v == highest:
                print( "{} -- {}".format(v, k))
def main():
    new_file = Input()
    wordlist = new_file.wordlist()
    new_input = Ngrams()
    new_input.process_wordlist(wordlist)
    new_input.print_max_ngrams()
main()
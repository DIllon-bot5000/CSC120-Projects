"""
    File: word-search.py
    Author: Dillon Barr
    Purpose: Reads in a word grid as well as a list of valid words and
             searches the grid to see if there are any matches and outputs the results.
    Course: CSC 120 Section: 001A Semester: Spring 2019
"""

def main():
    word_list = []
    grid_list = []
    found_words = []
    open_files(word_list, grid_list)
    search_horizontal(grid_list, word_list, found_words)
    search_vertical(grid_list, word_list, found_words)
    search_diagonal(grid_list, word_list, found_words)
    found_words = sorted(found_words)
    for i in found_words:
        print(i)

def open_files(word_list, grid_list):
    '''
    This function opens a file containing a list of words
    and a file containing a list of characters. It stores the words
    in a list and the characters into a list of lists.
    
    Parameters: word_list and grid_list are both lists.
    Returns: word_list populated with strings and grid_list as
     a list of lists containing characters.
    Pre-condition: word_list and grid_list are lists.
    Post-condition: word_list as a list and grid_list as a
                    list of list.
    '''
    
    word_file =input() #'words.txt' 
    word = open(word_file).readlines()
    for line in word:
        line = line.strip()
        word_list.append(line)
    
    grid_file =input() #'grid.txt' 
    grid = open(grid_file).readlines()
    for line in grid:
        line = line.strip().split()
        grid_list.append(line)

def search_horizontal(grid_list, word_list, found_words):
    '''
    This function takes a list of lists, a list of words and
    a list of matching words and checks to see if any of the 
    characters in the list of lists matches a word in the word list by
    calling another function to run the check.
    
    Parameter:  word_list and found_words are lists,
                grid_list is a list of lists containing characters.
    Pre-condition: word_list and found_words are lists, grid_list
                   is a list of lists.
    '''
    for i in grid_list:
        for j in range(len(i)):
            counter = 3
            while counter <= len(i):
                word = ''
                word += ''.join(i[j:j+counter])
                occurs_in(word, word_list, found_words)
                counter += 1
    for i in grid_list:
        reverse_list = []
        reverse_list = (list(reversed(i)))
        for j in range(len(i)):
            counter = 3
            while counter < len(i):
                word = ''
                word += ''.join(reverse_list[j:j+counter])
                occurs_in(word, word_list, found_words)
                counter += 1
                
def search_vertical(grid_list, word_list, found_words):
    '''
    This function takes a list of lists, a list of words and
    a list of matching words and checks to see if any of the 
    characters in the list of lists matches a word in the word list by
    calling another function to run the check.
    
    Parameter:  word_list and found_words are lists,
                grid_list is a list of lists containing characters.
    Pre-condition: word_list and found_words are lists, grid_list
                   is a list of lists.
    '''
    index = 0
    for i in grid_list:
        column = []
        for j in range(len(i)):
            column.append(grid_list[j][index])
        check_vertical(column, word_list, found_words)
        index += 1
        
    counter = 0
    for i in grid_list:
        column = []
        for j in range(len(i)):
            column.append(grid_list[j][counter])
        check_vertical((list(reversed(column))), word_list, found_words)
        counter += 1

            
def check_vertical(column, word_list, found_words):
    '''
    This function takes a list from the search_vertical function, 
    a list of found words so far and a list of matching words and checks to 
    see if any of the characters in the column list 
    matches a word in the word list by calling another function 
    to run the check.
    
    Parameter:  column, word_list and found_words are lists.
    Pre-condition: column, word_list and found_words are lists.
    '''
    for i in range(len(column)):
        counter = 3
        while counter <= len(column):
            word = ''
            word += ''.join(column[i:i+counter])
            occurs_in(word, word_list, found_words)
            counter += 1
            
def search_diagonal(grid_list, word_list, found_words):
    '''
    This function takes a list of lists, a list of words and
    a list of matching words and checks to see if any of the 
    characters in the list of lists matches a word in the word list by
    calling another function to run the check.
    
    Parameter:  word_list and found_words are lists,
                grid_list is a list of lists containing characters.
    Pre-condition: word_list and found_words are lists, grid_list
                   is a list of lists.
    '''
    index = 0
    diag = []
    for i in range(len(grid_list)):
        diag.append(grid_list[i][index])
        for j in range(len(diag)):
            counter = 3
            while counter < len(diag):
                word = ''
                word += ''.join(diag[j:j+counter])
                occurs_in(word, word_list, found_words)
                counter += 1
        index += 1
        
        

def occurs_in(s, L, found):
    '''
    This function takes a string, list of valid words, and a list
    of the words found so far.
    Parameter:  s is a string, L is the list of valid words,
                and found is the list of words found thus far.
    Pre-condition: s is a string, L and found are lists.
    Post-condition: if valid, found_words becomes more populated.
    '''
    if s in L and s not in found:
        found.append(s)
        

    
main()
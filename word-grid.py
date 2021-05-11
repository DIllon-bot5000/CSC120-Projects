"""
    File: word-grid.py
    Author: Dillon Barr
    Purpose: Takes in a randomly generated grid of numbers, converts
             to letters and then prints out the results in a grid format.
    Course: CSC 120 Section: 001A Semester: Spring 2019
"""
import random
import string



def main():
    init()
    

def init():
    '''
    This function takes input for the grid size, as well
    as the seed value and then calls a function to create the grid.
    
    '''
    N = int(input())
    S = input()
    random.seed(S)
    make_grid(N)

    
def make_grid(N):
    '''
    This function takes an integer and creates a multidimensional list
    filled with characters corresponding to the number values. It then
    calls another function to print the grid.
    
    Parameters: N is an integer value.
    Pre-condition: N is an integer.
    '''
    new_list = []
    for i in range(0, N):
        row = []
        for j in range(0, N):
            new_int = random.randint(0, 25)
            letter = number2letter(new_int)
            row.append(letter)
        new_list.append(row)
    print_grid(new_list)

def number2letter(num):
    '''
    This function returns a character corresponding to
    the number value received.
    Parameter: num is an integer value
    Returns: a corresponding ascii character.
    Pre-condition: num is an integer.
    Post-condition: returns an ascii character.
    '''
    return string.ascii_letters[num]

def print_grid(grid):
    '''
    This function takes a multidimensional list and 
    prints the list elements in a grid shape.
    
    Parameter: grid is a multidimesional list.
    Pre-condition: grid is a list.
    Post-condition: a grid shaped representation of the list.
    '''
    for i in grid:
        for j in range(len(i)):
            if j == len(i) - 1:
                print(i[j])
            else:
                print(i[j] + ',' , end = '')
main()
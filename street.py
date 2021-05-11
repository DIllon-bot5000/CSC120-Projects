'''
Created on Apr 16, 2019

@author: dbarr


'''
import string

class Building:
    '''
    Creates an object referring to a building read in from the user input.
    '''
    def __init__(self, width, height, brick):
        self._width = int(width)
        self._height = int(height)
        self._brick = brick
    def at_height(self, height):
        if height >= self._height:
            return ' ' * self._width
        else:
            return self._brick * self._width
    def get_width(self):
        return self._width

class Park:
    '''
    Creates an object referring to a building read in from the user input.
    '''
    def __init__(self, width, tree):
        self._width = int(width)
        self._tree = tree
    def get_width(self):
        return self._width
    def at_height(self, height):
        if height >= 5:
            return ' ' * self._width
        elif height == 4:
            return (' ' * (self._width // 2)) + self._tree + (' ' * (self._width // 2))
        elif height == 3:
            return (' ' * (self._width // 2 - 1)) + (self._tree * 3) + (' ' * (self._width // 2 - 1))
        elif height == 2:
            return (' ' * (self._width // 2 -2)) + self._tree * 5 + (' ' * (self._width // 2 -2))
        elif height == 1:
            return (' ' * (self._width // 2)) + '|' + (' ' * (self._width // 2))
        elif height == 0:
            return (' ' * (self._width // 2)) + '|' + (' ' * (self._width // 2))
        

class EmptyLot:
    '''
    Creates an object referring to an empty lot read in from the user input.
    '''
    def __init__(self, width, trash):
        self._width = int(width)
        self._trash = trash.replace('_', " ")
    def at_height(self, height):
        if height > 0:
            return ' ' * self._width
        elif height == 0:
            return self._trash * self._width
    
def main():
    schematic = input('Street: ')
    cleaner = schematic.replace(',', ' ')
    cleanest = cleaner.replace(':', ' ', 3)
    cleanest = cleanest.strip().split()
    object_list = create_objects_and_list(cleanest)
    max_height = max(get_height(cleanest))
    max_width = get_width(cleanest)
    print('+' + '-' * max_width + '+')
    print_street_at_height(object_list, max_height, max_width)
    
def create_objects_and_list(input_list):
    '''
    Takes a list and recursively creates objects based on the user input.
    
    Parameters: input_list is the list of the string the user input.
    
    Pre-condition: A valid string has been read in.
        
    Post-condition: a list of objects is created.
                    
    Returns: a list of objects.
    '''
    if input_list == []:
        return []
    if input_list[0] == 'b':
        building = Building(input_list[1], input_list[2], input_list[3])
        return [building] + create_objects_and_list(input_list[4:])
    if input_list[0] == 'p':
        park = Park(input_list[1], input_list[2])
        return [park] + create_objects_and_list(input_list[3:])
    if input_list[0] == 'e':
        empty_lot = EmptyLot(input_list[1], input_list[2])
        return [empty_lot] + create_objects_and_list(input_list[3:])

def get_height(input_list):
    '''
    Recursively goes through the input list to get the heights of each.
    
    Parameters: input_list is the list of the string the user input.
    
    Pre-condition: a valid string has been read in.
        
    Post-condition: a list with the various heights is returned.
                    
    Returns: a list of heights.
    '''
    if input_list == []:
        return []
    if input_list[0] == 'b':
        return [int(input_list[2])] + get_height(input_list[4:])
    if input_list[0] == 'p':
        return [5] + get_height(input_list[3:])
    if input_list[0] == 'e':
        return [1] + get_height(input_list[3:])

def get_width(input_list):
    '''
    Takes a list and sums the widths to find the max width.
    
    Parameters: input_list is the list of the string the user input.
    
    Pre-condition: A valid string has been read in.
        
    Post-condition: the max width is found
                    
    Returns: the max width
    '''
    if input_list == []:
        return 0
    if input_list[0] == 'b':
        return int(input_list[1]) + get_width(input_list[4:])
    if input_list[0] == 'p':
        return int(input_list[1]) + get_width(input_list[3:])
    if input_list[0] == 'e':
        return int(input_list[1]) + get_width(input_list[3:])

def print_street_at_height(object_list, max_height, max_width):
    '''
    Recursively starts at the max height and then prints each line on the way down.
    
    Parameters: object_list is a list of objects, max_height is the max height of the picture
                and the max_width is the width of the picture.
    
    Pre-condition: A valid string is read in, a list created, and the height and width found.
        
    Post-condition: the pictured specified is printed.
                    
    Returns: None
    '''
    if max_height == -1:
        print('+' + '-' * max_width + '+')
    else: 
        new_string = print_objects(object_list, max_height)
        print('|' + new_string + '|')
        max_height -= 1
        print_street_at_height(object_list, max_height, max_width)

def print_objects(object_list, max_height):
    '''
    Recursively goes through the list of objects and prints the necessary string
    at each height
    
    Parameters: object_list is a list and the height is an integer.
    
    Pre-condition: A valid string is read in, a list created, and the height and width found.
        
    Post-condition: a string of the various parts of the objects is returned.
                    
    Returns: a string of the user input structures.
    '''
    if object_list == []:
        return ''
    else:
        return str(object_list[0].at_height(max_height)) + print_objects(object_list[1:], max_height)
    
    

main()
"""
    File: pokemon.py
    Author: Dillon Barr
    Purpose: Compute the maximum average values for various Pokemon attributes 
        and answer queries about them.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""





def main():
    pokedex = {}
    type_averages = {}
    file_name = input() 
    open_file(file_name, pokedex)
    type_averages = get_type_averages(pokedex)
    user_queries(type_averages)
    
def open_file(file_name, dictionary):
    """ 
    Opens a CSV file and stores the contents into a 2-D dictionary.
  
    Parameters: file_name is a user input string and dictionary is an empty
                dictionary.
  
    Returns: A dictionary populated with Pokemon and their values.
  
    Pre-condition: file name is a string, dictionary is a dictionary.
  
    Post-condition: The return value is a dictionary.
    """
    file = open(file_name)
    for line in file:
        if line[0] == '#':
            continue
        line = line.strip().split(',')
        key = line[2]
        tempkey = line[1]
        stats = line[4:11]
        tempdict = {}
        tempdict[tempkey] = stats
        if key in dictionary:
            dictionary[key].update(tempdict)
        else:
            dictionary[key] = tempdict
    return dictionary

def get_type_averages(dictionary):
    """
    Loops through the dictionary of pokemon and adds the values of each Pokemon
    to a new dictionary broken down by types that also contains the average values
    for each type.
  
    Parameters: dictionary is the 2-D dictionary filled with individual Pokemon
    and their stats.
  
    Returns: A dictionary populated with Pokemon types and their average stats.
  
    Pre-condition: dictionary is a dictionary.
  
    Post-condition: The return value is a dictionary..
    """
    type_averages = {}
    for key1 in dictionary:
        empty_list = [0, 0, 0, 0, 0, 0, 0]
        average_list = []
        for key2 in dictionary[key1]:
            for stat_list in range(len(dictionary[key1][key2])):
                empty_list[stat_list] += int(dictionary[key1][key2][stat_list])
        
        for element in empty_list:
            element = element / len(dictionary[key1])
            average_list.append(element)
        type_averages[key1] = average_list
    return type_averages

def user_queries(type_averages):
    """
    Prompts the user for input and then calls another function to provide
    the needed data. Terminates when an empty line is entered.
  
    Parameters: type_averages is a dictionary populated with Pokemon types
                and their average stats.
  
    Returns: None
  
    Pre-condition: type_averages is a dictionary.
  
    Post-condition: None
    """
    terminate = ''
    user_query = input().lower()
    while user_query != terminate:
        if user_query == 'total':
            find_max_averages(type_averages, 0)
            user_query = input().lower()
        elif user_query == 'hp':
            find_max_averages(type_averages, 1)
            user_query = input().lower()
        elif user_query == 'attack':
            find_max_averages(type_averages, 2)
            user_query = input().lower()
        elif user_query == 'defense':
            find_max_averages(type_averages, 3)
            user_query = input().lower()
        elif user_query == 'specialattack':
            find_max_averages(type_averages, 4)
            user_query = input().lower()
        elif user_query == 'specialdefense':
            find_max_averages(type_averages, 5)
            user_query = input().lower()
        elif user_query == 'speed':
            find_max_averages(type_averages, 6)
            user_query = input().lower()
        else:
            user_query = input().lower()
    
        

def find_max_averages(type_averages, n):
    """
    Goes through the type_averages dictionary and finds the max value. It then
    prints the type and value of the max Pokemon and stat.
  
    Parameters: type_averages is a dictionary filled with Pokemon types
                and stats. N is an integer correlating to an index containing
                the info the user requested.
  
    Returns: None.
  
    Pre-condition: type_averages is a dictionary and n is an integer.
  
    Post-condition: None.
    """
    pokemon_type = ''
    max_average = 0
    max_dict = {}
    for k,v in type_averages.items():
        if v[n] >= max_average:
            max_average = v[n]
            pokemon_type = k
            max_dict[pokemon_type] = max_average
    maximum = max(max_dict, key=max_dict.get)
    print("{}: {}".format(maximum, max_dict[maximum]))
    
    
main()
    
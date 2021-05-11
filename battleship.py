"""
    File: battleship.py
    Author: Dillon Barr
    Purpose: Reads in a file containing the placements of one player's ships in a 
             game of Battleship. Proceeds to read in a file of guesses and barring
             any errors plays a game of Battleship.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""

import sys
class GridPos:
    '''
    This class represents data in each individual grid in a 2D list.
    '''
    def __init__(self,x,y,ship):
        '''
        Initializes the values of the data in each grid position.
         
        Parameters: x and y are integer values and ship is a string.
        
        Pre-condition: GridPos has been called.
        
        Post-condition: The data for a grid position has been initialized.
                    
        Returns: None
        '''
        self._x = x
        self._y = y
        self._ship = ship
        self._guessed = 0
    
    def __str__(self):
        if self._ship == None:
            return "N"
        else:
            return self._ship.kind


class Ship:
    '''
    This class represents a ship game piece used for playing Battleship.
    '''
    def __init__(self,list, raw):
        '''
        Initializes the attributes for each Ship object.
         
        Parameters: list is the split line from the file and raw is the raw line from the file.
        
        Pre-condition: The Ship class has been called.
        
        Post-condition: A Ship object is created.
                    
        Returns: None
        '''
        self._kind = list[0]
        self._x_start = int(list[1])
        self._y_start = int(list[2])
        self._x_end = int(list[3])
        self._y_end = int(list[4])
        self._raw = raw
        self._grid_positions = []
        self.fill_grid_positions()
        self.check_validity()
    
    def fill_grid_positions(self):
        '''
        This method finds the size of the ship, if it has been hit and the grid positions
        a ship occupies on the board.
         
        Parameters: None
        
        Pre-condition: A Ship object has been initialized.
        
        Post-condition: The ship size and health are set, and a list containing tuples of the occupied
                        grid positions is filled.
                    
        Returns: None
        '''
        if self._x_start != self._x_end and self._y_end != self._y_start:
            print("ERROR: ship not horizontal or vertical: " + self._raw)
            sys.exit(1)
        if self._x_start == self._x_end:
            self._size = abs(self._y_start-self._y_end)+1
            self._health = abs(self._y_start - self._y_end) + 1
            for i in range(self._size):
                if self._y_start < self._y_end:
                    self._grid_positions.append((self._x_start,self._y_start + i))
                else:
                    self._grid_positions.append((self._x_start, self._y_end + i))
        else:
            self._size = abs(self._x_start - self._x_end) + 1
            self._health = abs(self._x_start - self._x_end) + 1
            
            for i in range(self._size):
                if self._x_start < self._x_end:
                    self._grid_positions.append((self._x_start + i, self._y_start))
                else:
                    self._grid_positions.append((self._x_end + i, self._y_start))
    
    def check_validity(self):
        '''
        This method checks to see that the given ship matches the legal size for the ship type.
         
        Parameters: None
        
        Pre-condition: A ship object has been initialized.
        
        Post-condition: None
                    
        Returns: None
        '''
        if (self._kind == 'A' and self._size != 5) or (self._kind == 'B' and self._size != 4) or \
        (self._kind == 'S' and self._size != 3) or (self._kind == 'D' and self._size != 3) or \
        (self._kind == 'P' and self._size != 2):
            print( "ERROR: incorrect ship size: " + self._raw)
            sys.exit(1)
    
    def __str__(self):
        return self._kind

class Board:
    '''
    This class represents the player 1's side of the board during the game.
    '''
    def __init__(self, ship_list,grid):
        '''
        Initializes a Board object.
         
        Parameters: a list containing ship objects and a grid
                    containing a 2D list of GridPos objects.
        
        Pre-condition: The Board class has been called.
        
        Post-condition: None
                    
        Returns: None
        '''
        self._ship_list = ship_list
        self._grid = grid
    
    def guess(self,x,y):
        '''
        This method handles the actual playing of the game. It checks if the guess is valid to start
        and then checks if a ship occupies that spot. If it does the ship loses some health until it is
        sunk.
         
        Parameters: x and y are integer values read in from the guess file.
        
        Pre-condition: The Board class has been called and an object created.
        
        Post-condition: None
                    
        Returns: None
        '''
        if x > 9 or y > 9 or x < 0 or y < 0:
            print("illegal guess")
        else:
            gridpos = self._grid[x][y]
            if gridpos._ship == None:
                if gridpos._guessed != 0:
                    print("miss (again)")
                else:
                    print("miss")
                gridpos._guessed = 1
            else:
                if gridpos._guessed != 0:
                    print("hit (again)")
                else:
                    gridpos._ship._health -= 1
                    if gridpos._ship._health == 0:
                        print("{} sunk".format(gridpos._ship))
                    else:
                        print("hit")
                gridpos._guessed = 1

def main():
    try:
        filename = input()
        placement_file = open(filename).readlines()
    except IOError:
        print("ERROR: Could not open file: " + filename)
        sys.exit(1)
    try:
        filename = input()
        guess_file = open(filename).readlines()
    except IOError:
        print("ERROR: Could not open file: " + filename)
        sys.exit(1)
    process_files(placement_file, guess_file)

def process_files(placement_file, guess_file):
    '''
        This function takes the established valid input files and begins to process and create Ship objects.
        It also checks to see if any of the values from the placement file would cause errors and exit.
         
        Parameters: placement_file and guesss_file are the user input files containing ship positions
                    and user guesses.
        
        Pre-condition: The placement_file and guess_file have been input and found valid.
        
        Post-condition: Ship objects are created and then another function is called.
                    
        Returns: None
        '''
    ship_list = []
    for line in placement_file:
        raw = line
        line = line.split()
        new_ship = Ship(line, raw)
        for number in line[1:5]:
            if int(number) >9 or int(number)<0:
                print("ERROR: ship out-of-bounds: " + raw)
                sys.exit(1)
        if new_ship not in ship_list:
            ship_list.append(new_ship)
        elif new_ship in ship_list:
            print("ERROR: fleet composition incorrect")
            sys.exit(1)
    if len(ship_list) != 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(1)
    create_grid(ship_list, guess_file)

def create_grid(ship_list, guess_file):
    '''
        This function creates the 10x10 grid used to play the game and then checks the placements
        of the ships to make sure they are in valid positions.
         
        Parameters: ship_list is a list of Ship objects created in the prior functions and guess_file
        is the user input file of guess.
        
        Pre-condition: The files have been read in with no error and the Ship objects have been created with 
        no errors. 
        
        Post-condition: The grid used for the game has been created and the game can commence.
                    
        Returns: None
        '''
    grid = []
    for i in range(10):
        column = []
        for j in range(10):
            position_info = None
            for ship in ship_list:
                assert len(ship_list) != 0, 'Empty list'
                if (i,j) in ship._grid_positions:
                    if position_info != None:
                        print("ERROR: overlapping ship: " + ship._raw)
                        sys.exit(1)
                    position_info = GridPos(i,j,ship)

            if position_info == None:
                position_info = GridPos(i,j,None)
            column.append(position_info)
        grid.append(column)
    play_game(ship_list, grid, guess_file)

def play_game(ship_list, grid, guess_file):
    '''
        This function creates the board object and processes the guess file to actually play the game.
         
        Parameters: ship_list is the list of SHip objects, grid is the 2D list of GridPos objects and
                    guess_file is the user input file of guesses.
        
        Pre-condition: The 2D grid list has been created and no errors have occured with the Ship objects
                       or their placements on the board.
        
        Post-condition: The guess_file is read and the game is played until completion.
                    
        Returns: None
        '''
    game_board = Board(ship_list, grid)
    for line in guess_file:
        line = line.split()
        game_board.guess(int(line[0]),int(line[1]))
        surviving_ships = 0
        for ship in game_board._ship_list:
            assert len(game_board._ship_list) != 0, "Empty list."
            if ship._health != 0:
                surviving_ships += 1
        if surviving_ships == 0:
            print("all ships sunk: game over")
            sys.exit(1)

main()
"""
    File: bball.py
    Author: Dillon Barr
    Purpose: Finds the conference with the highest average win percentage and prints the results.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""
import sys

class Team:
    '''
    This class takes a line from the file being read in and creates an object
    with attributes made up of different parts of the line.
    '''
    def __init__(self, line):
        '''
        Takes a line from the file and initializes attributes made up of different parts
        of the line.
    
        Parameters: line is a list made up of a line from the file read in.
        
        Pre-condition: line is a list.
        
        Post-condition: attributes of the team object have been initialized.
                    
        Returns: none
        '''
        assert len(line) > 0, 'Empty file.'
        self._line = line
        self._name = self.name()
        self._win_ratio_str = self.win_ratio()
    def name(self):
        '''
        Takes the line attribute and loops through it from the end
         to find the first instance of ( and returns the elements 
         before it as a string of the team name.
         
        Parameters: line is a list made up of a line from the file read in.
        
        Pre-condition: line has been initialized in __init__.
        
        Post-condition: the self._name attribute is initialized.
                    
        Returns: the team name as  a string.
        '''
        for item in range(len(self._line)-1, -1, -1):
            if '(' in self._line[item]:
                self._placeholder = item
                break
        self._name = ' '.join(self._line[:self._placeholder])
        return self._name
    def conf(self):
        '''
        Takes the line attribute and loops through it from the end
         to find the first instance of ( and returns the elements 
         before it as a string of the conference name.
         
        Parameters: line is a list made up of a line from the file read in.
        
        Pre-condition: line has been initialized in __init__.
        
        Post-condition: the self._conference attribute is initialized.
                    
        Returns: the conference name as  a string.
        '''
        if ")" in self._line[self._placeholder]:
            self._conference = str(self._line[self._placeholder]).strip('()')
            return self._conference
        else:
            self._conference = ' '.join(self._line[self._placeholder: self._placeholder+2]).strip('()')
            return self._conference
    def win_ratio(self):
        '''
        Takes the line attribute and loops through it from the end
         to find the first instance of ) and computes the win ratio
         using the integers afterwards. Returns the win ratio as a string.
         
        Parameters: line is a list made up of a line from the file read in.
        
        Pre-condition: line has been initialized in __init__.
        
        Post-condition: the self._win_ratio attribute is initialized.
                    
        Returns: the team win ratio as a string.
        '''
        for item in range(len(self._line)-1, -1, -1):
            if ')' in self._line[item]:
                marker = item
                break
        assert (int(self._line[marker+1]) + int(self._line[marker+2])), 'Cannot divide by 0.'
        win_ratio = int(self._line[marker+1]) / (int(self._line[marker+1]) + int(self._line[marker+2]))
        self._win_ratio_str = str(win_ratio)
        return self._win_ratio_str
    def __str__(self):
        return ("{} : {}".format(self._name, self._win_ratio_str))

class Conference:
    '''
    This class creates and object representing the conference and contains a list
    of teams in the conference.
    '''
    def __init__(self, conf):
        '''
        Takes the name of a conference and creates an attribute of that conference as well
        as initalizes a list to hold team objects of teams in that conference.
         
        Parameters: conf is a string created in the Team class.
        
        Pre-condition: a Team object has been created.
        
        Post-condition: a Conference object is created and a list initialized.
                    
        Returns: none
        '''
        self._conf = conf
        self._team_list = []
    def contains(self, team):
        '''
        Checks to see if a team is in the team_list and returns True or False.
         
        Parameters: team is a Team object.
        
        Pre-condition: a Team object has been created.
        
        Post-condition: none
                    
        Returns: True or False
        '''
        if team not in self._team_list:
            return False
        return True
    def name(self):
        '''
        Getter method
        '''
        return self._conf
    def add(self, team):
        '''
        Adds a team object to the team_list.
         
        Parameters: team is a Team object.
        
        Pre-condition: a Team object has been created,
        
        Post-condition: the team_list length increases by 1.
                    
        Returns: a list of team objects in the correct conference..
        '''
        self._team_list.append(team)
        return self._team_list
    def win_ratio_avg(self):
        '''
        Loops through the list of teams in a conference and calculates the average win ratio
        of that conference.
         
        Parameters: none passed in.
        
        Pre-condition: the length of the team_list > 0
        
        Post-condition: the avg win ratio of the conference is calculated.
                    
        Returns: the average win ratio of a conference.
        '''
        team_averages = 0
        for teams in self._team_list:
            team_averages += float(teams.win_ratio())
        win_ratio_avg = team_averages / len(self._team_list)
        return win_ratio_avg
    def __str__(self):
        return "{} : {}".format(self._conf, self.win_ratio_avg())
    
class ConferenceSet:
    '''
    This class creates an object that will hold a list of all the conference
    objects created while reading the input file.
    '''
    def __init__(self):
        '''
        Creates a list to hold the conference objects.
         
        Parameters: none
        
        Pre-condition: none
        
        Post-condition: a list is created.
                    
        Returns: none
        '''
        self._list = []
    def add(self, team):
        '''
        Takes a team object and checks to see if an object with that conference
        name exists in the list. If it does it appends the team to the corresponding list,
        otherwise creates a new conference object to hold the team.
        
        Parameters: team is a Team object created while looping through the file.
        
        Pre-condition: a team object has been created.
        
        Post-condition: the team has been appended to a confernce object's list.
                    
        Returns: none
        '''
        counter = 0
        conference = team.conf()
        new_conf = Conference(conference)
        if len(self._list) > 0:
            for item in self._list:
                if item.name() == new_conf.name():
                    item.add(team)
                    counter += 1
        if counter == 0:
            new_conf.add(team)
            self._list.append(new_conf)
          
    def best(self):
        '''
        Loops through the list of conference objects and calculates the conferences 
        avg win ratio. It then adds the conference name and ratio to a dictionary and 
        returns the max win percentage and the corresponding conference. I know that creating
        and using this extra dictionary was not necessary but I couldn't figure out how to do it
        without it so if you can leave a note on what I was supposed to do or explain it in an email I
        would appreciate it.
         
        Parameters: none passed in.
        
        Pre-condition: the list created in the ConferenceSet class is populated
                       with Conference objects.
        
        Post-condition: none.
                    
        Returns: the highest avg win ratio and its conference.
        '''
        ratio_dict = {}
        for conference in self._list:
            ratios = conference.win_ratio_avg()
            ratio_dict[conference.name()] = ratios
        highest = max(ratio_dict.values())
        for key, values in ratio_dict.items():
            if values == highest:
                print( "{} : {}".format(key, values))
            
    
def main():
    conference_set = ConferenceSet()
    open_file(conference_set)
    
def open_file(conference_set):
    '''
        Opens the a file from user input and loops through the file
        to create Team objects, which in turn are added to the ConferenceSet class
        which creates Conference obejcts.
         
        Parameters: conference_set is a ConferenceSet object initialized in main.
        
        Pre-condition: conference_set has been initialized.
        
        Post-condition: The file has been read and the highest avg win ratio printed.
                    
        Returns: the highest avg win ratio and its conference.
        '''
    file_name = input()
    try:
        file = open(file_name)
    except IOError:
        print("ERROR: Could not open file " + file_name)
        sys.exit(1)
    for line in file:
        if line[0] == '#':
            continue
        line = line.rstrip().split()
        team = Team(line)
        conference_set.add(team)
    return (conference_set.best())
        

main()
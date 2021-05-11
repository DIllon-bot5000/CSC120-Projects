'''
Created on Feb 11, 2019

@author: dbarr
'''
class Date:
    '''
    This class takes in two strings representing a date and another
    representing an event.  
    
    '''
    def __init__(self, date, event):
        '''
        Takes in two strings, one for a date and one as an event and creates 
        the instances of those variables.
    
        Parameters: date is a string in a yyyy-mm-dd format and event
                    is a string detailing an event on that date.
                    
        Returns: none
        '''
        self._date = date
        self._event = event
        self._eventlist = []
    def add_event(self, event):
        '''
        This method adds the event to a list associated with the date taken in as well.
        
        Parameters: event is a string.
        
        Returns: None
        '''
        self._eventlist.append(event)
    def get_date(self):
        return self._date
    def get_event(self, event):
        return self._event
    def get_eventlist(self):
        return self.eventlist
    def __str__(self):
        return self._date + str(self._eventlist)
    
class DateSet:
    '''
    This class creates a dictionary consisting of dates as keys
    and the Date objects as the values.
    
    '''
    def __init__(self):
        '''
        Creates aempty dictionary to be filled later with 
    
        Parameters: Takes in nothing but creates an empty dictionary to be populated.
                    
        Returns: None
        '''
        self._dict = {}
    def add_date(self, date, event):
        '''
        Takes a date and event and creates an object in the Date class. Then the object is stored
        in the dictionary for use later.
    
        Parameters: Takes in two strings, date and event.
                    
        Returns: None
        '''
        new_date = Date(date, event)
        new_date.add_event(event)
        if date not in self._dict:    
            self._dict[date] = []
        self._dict[date].append(new_date.get_event(event))
    def print_events(self, date):
        for key, values in self._dict.items():
            if date == key:
                for items in sorted(values):
                    print("{}: {}".format(key, items))
                
        def __str__(self):
            for key, values in self._dict.items():
                print(key, values)
def main():
    open_file()

def canonicalize_date(date_str):
    '''
    This function takes in a string representing a date and returns the same date in a canonical
    representation of yyyy-mm-dd.
    
    Parameters: date_str is a string representing a date.

    Returns: a new string in the canonical form of yyyy-mm-dd.
    '''
    if '-' in date_str:
        new_date = date_str.split('-')
        assert int(new_date[1]) <= 12 and int(new_date[2]) <= 31, 'Error: Illegal date.'
        canon_date = ("{:d}-{:d}-{:d}".format(int(new_date[0]), int(new_date[1]), int(new_date[2])))
        return canon_date
    elif '/' in date_str:
        new_date = date_str.split('/')
        assert int(new_date[0]) <= 12 and int(new_date[1]) <= 31, 'Error: Illegal date.'
        canon_date = ("{:d}-{:d}-{:d}".format(int(new_date[2]), int(new_date[0]), int(new_date[1])))
        return canon_date
    else:
        month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        new_date = date_str.split()
        new_month = month_list.index(new_date[0]) + 1
        assert int(new_month) <= 12 and int(new_date[1]) <= 31, 'Error: Illegal date.'
        canon_date = ("{:d}-{:d}-{:d}".format(int(new_date[2]), int(new_month), int(new_date[1])))
        return canon_date
    
def open_file():
    '''
        Opens a user input file. Reads the lines of the file and manipulates the lines
        so that the date is in one variable and the event is in the other. If the line starts with 'I' the
        the variables are sent to DataSet to be stored or created as a Data object if they do not exist.
        If the line starts with 'R' it calls a method to print out the appropriate info from the
        DataSet class.
    
        Parameters: None
                    
        Returns: None
    '''
    data = DateSet()
    file_name = input()
    file = open(file_name)
    for line in file:
        assert line[0] == 'I' or 'R', "Error: Illegal operation."
        if line[0] == 'I':
            line = line.strip().split(':', 1)
            date = canonicalize_date(line[0].strip('I').strip())
            event= line[1].strip()
            data.add_date(date, event)
        elif line[0] == 'R':
            line = line.strip().split()
            if '-' or '/' not in line:
                string_date = ' '.join(line[1:])
                date = canonicalize_date(string_date)
                data.print_events(date)
            else:
                date = canonicalize_date(line[1])
                data.print_events(date)
main()
        
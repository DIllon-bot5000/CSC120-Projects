"""
    File: fake-news.py
    Author: Dillon Barr
    Purpose: Reads in a csv file and prints the most used words based on user input.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""
import csv
import string

class Node:
    '''
    This class creates a node object populated with data from the 
    input file that will be put in a linked list object later.
    '''
    def __init__(self, word):
        self._word = word
        self._count = 1
        self._next = None
    def word(self):
        #returns the word associated with the node
        return self._word
    def count(self):
        #returns the count associated with the word of the node
        return self._count
    def next(self):
        #returns the next attribute
        return self._next
    def set_next(self, target):
        self._next = target
    def incr(self):
        #increments the count of the word in the node
        self._count += 1
    def __str__(self):
        pass

class LinkedList:
    '''
    This class creates a linked list that will contain node objects containing data
    about the words being read in from the file.
    '''
    def __init__(self):
        '''
        Initializes the head of the linked list object setting it to None.
         
        Parameters: None
        
        Pre-condition: The LinkedList class has been called.
        
        Post-condition: A LinkedList object has been created.
                    
        Returns: None
        '''
        self._head = None
    def is_empty(self):
        #returns True if the LinkedList is empty, False otherwise.
        if self._head == None:
            return True
        return False
    def head(self):
        #returns the head of the LinkedList.
        return self._head
    def add(self, node):
        #taken from the short assignments.
        node._next = self._head
        self._head = node
    def update_count(self, word):
        '''
        Updates the count of the node object containing the string word, otherwise
        creates a new node object and adds it to the head of the LinkedList.
         
        Parameters: word is a string word read in from the file.
        
        Pre-condition: A valid file has been opened, the title cleaned, and a LinkedList exists.
        
        Post-condition: A node object is created or the count is updated.
                    
        Returns: None
        '''
        if self.find(word) == True:
            current = self._head
            while current != None:
                if current._word == word:
                    current.incr()
                current = current._next         
        else:
             word= Node(word)
             self.add(word)
    def find(self, item):
        #taken from the short assignments
        current = self._head
        while current != None:
            if current._word == item:
                return True
            current = current._next
        return False
    def rm_from_head(self):
        #taken from the short assignments
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    def insert_after(self, node1, node2):
        #taken from the short assignments
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    def sort(self):
        '''
        Creates a new LinkedList and removes nodes from the initial LinkedList and puts them into the new LinkedList
        sorting them in descending order.
         
        Parameters: None
        
        Pre-condition: A valid file has been opened, the title cleaned, a LinkedList exists and is populated
                       with node objects containing words and their counts.
        
        Post-condition: The initial elements in the LinkedList are now sorted in descending order.
                    
        Returns: None
        '''
        sorted = LinkedList()
        while self._head != None:
            current_elem = self.rm_from_head()
            if sorted._head == None:
                sorted._head = current_elem
            else:
                temp = sorted._head
                while temp != None:
                    if current_elem._count > temp._count:
                        E = temp
                        sorted._head = current_elem
                        sorted._head._next = E
                        break
                    if temp._count >= current_elem._count and temp._next == None or \
                    temp._next._count < current_elem._count:
                        sorted.insert_after(temp, current_elem)
                        break
                    temp = temp._next
        self._head = sorted._head

    def get_nth_highest_count(self, n):
        '''
        Takes the user input in and finds the word count associated with the node at n position.
         
        Parameters: N is the user input integer.
        
        Pre-condition: A valid file has been opened, the title cleaned, a LinkedList exists and is populated
                       with node objects containing words and their counts and the user input integer is valid.
        
        Post-condition: The word count at n node is stored in a variable for use in another method.
                    
        Returns: None
        '''
        self.sort()
        current = self._head
        counter = 0
        node = 0
        while current != None:
            if node - 1 == n:
                spot = prev._count
                self.print_upto_count(spot)
            prev = current
            current = current._next
            node +=1

    
        
        
    def print_upto_count(self, n):
        '''
        Prints out the words and their counts for all words greater than or equal to the count found in the previous method.
        
        Parameters: None
        
        Pre-condition: A valid file has been opened, the title cleaned, a LinkedList exists and is populated
                       with node objects containing words and their counts, the user integer is valid and the count
                       of the node in the previous method has been found.
        
        Post-condition: Prints out the words with higher or equal counts found in the node from the previous method.
                    
        Returns: None
        '''
        current = self._head
        while current != None:
            if current._count >= n:
                print("{} : {:d}".format(current._word, current._count))
            current = current._next
    
def open_file(llist):
    '''
    This function opens the csv file and reads in the contents to create the node elements used later.
         
    Parameters: llist is the empty LinkedList object created in main
    
    Pre-condition: The function has been called and a LinkedList has been created.
        
    Post-condition: The LinkedList has been populated with nodes.
                    
    Returns: The populated LinkedList.
    '''
    try:
        infilename = input('File: ')
        infile = open(infilename)
    except IOError:
        print("ERROR: Could not open file " + infilename)
        sys.exit(1)

    csvreader = csv.reader(infile)
    for itemlist in csvreader:
        if len(itemlist) == 1:
            break
        if  '#' in itemlist[0]:
            continue
        else:                                
            title = itemlist[4]
            no_punc_title = check_punc(title)
            no_punc_title = no_punc_title.strip().split()                
            cleanest_list = delete_small_words(no_punc_title)                
            llist = create_nodes(cleanest_list, llist)
    return llist
    infile.close()
    
def check_punc(new_list):
    '''
    Checks if there is punctuation in the strings comprising the titles of the articles and replaces the punctuation
    with spaces if they exist.
         
    Parameters: old_title is the string that may contain punctuation.
        
    Pre-condition: A valid file has been opened.
        
    Post-condition: A string with no punctuation is returned.
                    
    Returns: a string with no punctuation
    '''
    title = ''
    for char in new_list:
        title += char
        if char in string.punctuation:
            title = title.replace(char, ' ')
    return title

def delete_small_words(some_list):
    '''
    Takes the list of words read in from the file and cleaned and removes all strings with a length of 2 or less.
         
    Parameters: some_list is the list of words from the titles
    
    Pre-condition: a valid file has been read in and the punctuation stripped from the strings.
        
    Post-condition: The list does not cotain any elements with a length of 2 or less.
                    
    Returns: A list of strings all with lengths greater than 2.
    '''
    for i in range(len(some_list) - 1, -1, -1):
        if len(some_list[i]) <= 2:
            del some_list[i]
    return some_list

def create_nodes(new_list, llist):
    '''
    The function loops through the list of words and calls a method in the LinkedList to either create a new Node,
    or increment the count of a existing one.
         
    Parameters: new_list is a list of words read in from the file and llist is a LinkedList object.
        
    Pre-condition: a valid file has been read in and the elements stripped of spaces and punctuation and all the elements
                   have a length of more than 2.
        
    Post-condition: the LinkedList object is populated with Nodes.
                    
    Returns: a LinkedList object populated with Nodes.
    '''
    for item in new_list:
        item= item.lower()
        llist.update_count(item)
    return llist
        
def get_user_int(llist):
    '''
    Gets a valid integer input from the user and uses that to determine the count of words that will be used
    to print out the output.
         
    Parameters: llist is a LinkedList object.
        
    Pre-condition: A valid file has been opened, titles cleaned, LinkedList populated and sorted.
        
    Post-condition: LinkList methods are called to ultimately print out the desired results.
                    
    Returns: None
    '''
    try:
        user_int = int(input('N: '))
    except:
        print("ERROR: Could not read N")
        sys.exit(1)
    assert user_int >= 0
    llist.sort()
    llist.get_nth_highest_count(user_int)
        
def main():
    llist = LinkedList()
    llist = open_file(llist)
    get_user_int(llist)

main()
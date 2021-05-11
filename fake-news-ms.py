import csv
import sys
import string

class Word:
    '''
    This class creates an object for each unique word in the file
    and counts the number of occurrences as well.
    '''
    def __init__(self,word):
        self._word = word
        self._count = 1
    def word(self):
        return self._word
    def count(self):
        return self._count
    def incr(self):
        self._count += 1
    def __str__(self):
        return self._word

def main():
    try:
        filename = input('File: ')
        file = csv.reader(open(filename))
    except IOError:
        print("ERROR: Could not open file " + filename)
        sys.exit(1)
    try:
        user_int = int(input('N: '))
    except:
        print("ERROR: Could not read N")
        sys.exit(1)
    mylist = []
    for line in file:
        if '#' not in line[0]:
            title = line[4].lower()
            for element in string.punctuation:
                if element in title:
                    title = title.replace(element," ")
            for word in title.split():
                if len(word)>2:
                    count_word(word,mylist)
    sorted_list = msort(mylist)
    i = 0
    while sorted_list[i].count() >= sorted_list[n].count():
        print("{} : {:d}".format(sorted_list[i], sorted_list[i].count()))
        i += 1
def count_word(word,mylist):
    '''
    Checks if a word object exists, if so the count is incremented by one, if not a new object is created.
         
    Parameters: word is string from the file and mylist is a list of word objects.
        
    Pre-condition: A valid file has been opened and a list created.
        
    Post-condition: The list is full and all the words properly incremented.
                    
    Returns: None
    '''
    found = False
    for element in mylist:
        if element.word() == word:
            element.incr()
            found = True
    if found == False:
        new_word = Word(word)
        mylist.append(new_word)

def msort(L):
    '''
    Takes a list and splits the list to sort the list into two sorted lists.
    
    Parameters: L is a list
    
    Pre-condition: A valid file has been opened and a list has been created.
        
    Post-condition: Ultimately the merge sorted list is returned.
                    
    Returns: Merge sorted list
    '''
    if len(L) <= 1:
        return L
    else:
        split_pt = len(L) // 2
        L1 = L[:split_pt]
        L2 = L[split_pt:]
        sortedL1 = msort(L1)
        sortedL2 = msort(L2)
        return merge(sortedL1 , sortedL2)
def merge(left,right):
    '''
    Creates a single merged list from the two lists passed in.
         
    Parameters: left and right are the lists created in the previous method.
        
    Pre-condition: A valid file has been opened, and two sorted lists have been created.
        
    Post-condition: A single merge sorted list exists.
                    
    Returns: A merge sorted list.
    '''
    if not len(left) or not len(right):
        return left or right
    result = []
    i,j = 0,0
    while (len(result)<len(left)+len(right)):
        if left[i].count() > right[j].count():
            result.append(left[i])
            i += 1
        elif left[i].count() == right[j].count():
            if str(left[i]) < str(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result
main()
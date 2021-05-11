"""
    File: huffman.py
    Author: Dillon Barr
    Purpose: Reads in a text file and uses the data inside to create a tree and use that to decode the final line.
    Course: CSC 120 Section: 1A Spring Semester 2019
"""
import sys
class Tree:
    '''
    This class creates a tree object that will be populated using the data
    read in from the input file.
    '''
    def __init__(self):
        self._value = None
        self._left = None
        self._right = None
    def add_value(self,value):
        self._value = value
    def __str__(self):
        return self._value
def main():
    open_file()

def open_file():
    '''
    Takes the user input for a file and opens the file if valid. Then calls other functions to create the tree, postorder and
    print out the decoded values.
         
    Parameters: None
        
    Pre-condition: None
        
    Post-condition: The decoded values from the input file.
                    
    Returns: None
    '''
    try:
        filename = input('Input file: ')
        file = open(filename).readlines()
    except IOError:
        print("ERROR: Could not open file " + filename)
        sys.exit(1)
    preorder = file[0].split()
    inorder = file[1].split()
    line = file[2]
    tree = Tree()
    build_tree(preorder,inorder,tree)
    print(postorder_str(tree)[1:])
    decoded = decode_func(tree,tree,line)
    print(decoded.strip('None'))
    
def build_tree(preorder,inorder,tree):
    '''
    Takes the preorder and inorder values from the file and populates the tree.
         
    Parameters: preorder and inorder are lines from the input file and tree is an empty tree object.
        
    Pre-condition: A valid file has been opened, preoder, inorder and empty tree created.
        
    Post-condition: a tree populated with values from the preoder and inorder.
                    
    Returns: a populated tree
    '''
    if len(preorder)>0:
        tree.add_value(preorder[0])
        left_in = inorder[:inorder.index(preorder[0])]
        right_in = inorder[inorder.index(preorder[0])+1:]
        left_pre = preorder[1:1+len(left_in)]
        right_pre = preorder[1+len(left_in):]
        if len(left_pre)>0:
            tree._left = Tree()
            build_tree(left_pre,left_in,tree._left)
        if len(right_pre)>0:
            tree._right = Tree()
            build_tree(right_pre,right_in,tree._right)
    else:
        return
def postorder_str(tree):
    '''
    Takes the populated tree and traverses through it to print out the postorder traversal of the tree.
         
    Parameters: tree is a populated tree object.
        
    Pre-condition: A valid file has been opened and a tree populated using the pre and inorder data from the file.
        
    Post-condition: The postorder traversal is created.
                    
    Returns: The postorder traversal.
    '''
    poststr = ''
    if tree._right != None:
        poststr += postorder_str(tree._right)+' '+ str(tree._value)
    else:
        poststr = " " + str(tree._value) + poststr
    if tree._left != None:
        poststr = postorder_str(tree._left)  + poststr
    return poststr
def decode_func(tree,tree1,line):
    '''
    Traverse the tree recursively to find the leaves of the tree and then creates the decoded string.
         
    Parameters: tree and tree1 are a tree and line is the third line in the input file.
        
    Pre-condition: A valid file has been opened and a tree created.
        
    Post-condition: The decoded string is created.
                    
    Returns: The decoded string.
    '''
    if len(line) == 0:
        if tree._left == None and tree._right == None:
            return str(tree._value)
        else:
            return ''
    elif len(line) > 0:
        if tree._left == None and tree._right == None:
            return (str(tree._value) + str(decode_func(tree1,tree1,line)))
        else:
            if line[0] == "0":
                    return (decode_func(tree._left,tree1,line[1:]))
            elif line[0] == "1":
                    return (decode_func(tree._right,tree1,line[1:]))

main()
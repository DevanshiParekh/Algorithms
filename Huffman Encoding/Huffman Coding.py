#-------------------------------------------------------------------------------
# Name:        Huffman Encoding
# Purpose:
#
# Author:      Devanshi
#
# Created:     10-04-2017
# Copyright:   (c) Devanshi 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from operator import itemgetter
from collections import OrderedDict

class Node:
    def __init__(self,name,freq):
        self.name=name
        self.freq=freq
        self.right=None
        self.left=None
        self.string=[]

#sorting elements of a class based on its freq
    def __lt__(self, other):
         return self.freq < other.freq


def Huffman_code(char,freq):
    #convert each element into Node
    elements=list(Node(char[i],freq[i] )for i in range(len(char)))

    #until we have our last element take the least elements and make a new node
    #append that node into the list which we already have
    while len(elements)!=1:
        elements.sort(reverse=True)
        a=elements.pop()
        b=elements.pop()
        z=Node('@',a.freq+b.freq)
        z.left=a
        z.right=b
        elements.append(z)
    root=elements.pop()
    display(root)

#display the route for each alphabet

def display(root):
       if root.left == None and root.right==None:
            print(root.name,"".join(str(x) for x in root.string))
       if root.left !=None:
            root.left.string=root.string+[0]
            display(root.left)
       if root.right !=None:
            root.right.string=root.string+[1]
            display(root.right)

#take the inputs from the user
char=list(input().split(" "))
freq=list(int(i) for i in input().split(" "))
Huffman_code(char, freq)

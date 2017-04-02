#-------------------------------------------------------------------------------
# Name:        Breadth First Search
#
# Author:      Devanshi
#
# Created:     02-04-2017
# Copyright:   (c) Devanshi 2017
# Licence:
#-------------------------------------------------------------------------------

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class BST:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        q=[root] if root else []
        while q:
            cur = q.pop()
            print(cur.data,end= " ")
            if cur.left:
                q.insert(0,cur.left)
            if cur.right:
                q.insert(0,cur.right)
T=int(input("Enter the number of nodes"))
myTree=BST()
root=None
for i in range(T):
    data=int(input("Enter the data"))
    root=myTree.insert(root,data)
myTree.levelOrder(root)

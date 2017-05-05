#-------------------------------------------------------------------------------
# Name:        NQueens: Improved solution
# Purpose:
#
# Author:      Devanshi
#
# Created:     05-05-2017
# Copyright:   (c) Devanshi 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
In this program we shall display yes and print the solution and if solution does
not exist we print no.

Logic:
    result is the list representing the row number , the value in it represents
    the column number.
    let x be the row and y be the col
    if x1=x2 : queens are in the same row , which we would not consider as we
    will move row-wise
    if y1=y2: queens are in the same col.
    if abs(x1-x2)=abs(y1-y2) then there is a queen present diagonally.

This code is optimal as it will follow the recursion the least number of times as
the comparison is done 1-D now.
'''

import sys
sys.setrecursionlimit(1000000000)
result=[]
count=0
def not_attacked(x,y,N):
    global result
    for i in range(x):
        if result[i]==y or abs(x-i)==abs(result[i]-y):
            return False
    return True

def NQueens(x,N):
    global result,board,count
    for i in range(N):
        if not_attacked(x,i,N):
            result[x]=i
            if x==N-1:
                board={ (i,j):0 for i in range(N) for j in range(N) }
                if count==0:
                    count=1
                if count==1:
                    print("YES")
                for i in range(N):
                    board[i,result[i]]=1
                new_board=sorted(board)
                n=0
                for i in new_board:
                    if n==N:
                        n=0
                        print()
                    print(board[i],end=" ")
                    n+=1
                print()
            if count==1:
                return
            NQueens(x+1,N)

N=int(input())
for i in range(N):
    result.append(100)
NQueens(0,N)
if count==0:
    print("NO")
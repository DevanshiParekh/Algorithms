#-------------------------------------------------------------------------------
# Name:        Nqueens (backtracking)
# Purpose:
#
# Author:      Devanshi
#
# Created:     29-04-2017
# Copyright:   (c) Devanshi 2017
#-------------------------------------------------------------------------------

import sys
#increasing stack capacity
sys.setrecursionlimit(10000000000)

#checking if queen is attacked
def is_attacked(row,col,board,N):
    for i in range(N):
        if board[row,i]==1 or board[i,col]==1:
            return True
    for i in range(N):
        for j in range(N):
            if board[i,j]==1:
                if i+j==row+col or i-j==row-col:
                    return True
    return False

# solving nqueens using backtrack
def NQueens(board,n,N):
    if n==0:
        return True
    for i in range(N):
        for j in range(N):
            if is_attacked(i,j,board,N):
                continue
            board[i,j]=1
            if NQueens(board,n-1,N):
                return True
            board[i,j]=0
    return False


N=int(input())
board={ (i,j):0 for i in range(N) for j in range(N) }

#if solved print the board
if NQueens(board,N,N):
    print("YES")
    new_board=sorted(board)
    n=0
    for i in new_board:
        if n==N:
            n=0
            print()
        print(board[i],end=" ")
        n+=1
else:
    print("NO")
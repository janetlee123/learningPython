# Input: list of lists demonstrating the 9x9 grid of a sudoku game 
# Output: solved sudoku puzzle in list of lists 

#Approach: attempt at filling in all the empty spots from 1-9 
# if it reaches the puzzles expected results, then returns the list 
# References: #https://stackoverflow.com/questions/74073701/how-to-check-every-3-x-3-box-in-sudoku
# https://medium.com/@ev.zafeiratos/sudoku-solver-with-python-a-methodical-approach-for-algorithm-optimization-part-1-b2c99887167f 

import random

def isvalid(num,pos,board): 
   # given the number to guess, its position on the board and the board 2D list
   # Returns true if num is not repeated in row, column or box 

    row,column = pos 
    
    #check if column contains num 
    for i in range(9): 
        if board[i][column] == num: 
            return False 
    
    #check if row contains num
    for j in range(9):
        if board[row][j] == num: 
            return False 
        
    #check if box contains num 
    firstrow= 3 * (row // 3 )
    firstcolumn = 3 * (row//3)
    
    for i in range(3):
        for j in range(3): 
            if board[firstrow+i][firstcolumn+j] == num:
                return False 
            
    #If num not contained in rows, columns or boxes
    return True 
                 
def isCorrect(possiblesolve):
    # Checks to see if the board with a possiblesolve is correct  
    def iscomplete(line):
        return len(set(line)) == 9
     
    if not all (iscomplete(rows)for rows in possiblesolve):
        return False 
        
    if not all(iscomplete([row[column] for row in possiblesolve]) for column in range(9)):
        return False 
    
    for row in range (0,3,6): 
        for column in range (0,3,6): 
            box = (possiblesolve[row][column:column+3] + 
                    possiblesolve[row+1][column:column+3]+
                        possiblesolve[row+2][column:column+3])
        if not iscomplete(box):
            return False 

    return True

def findblank(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return i,j    
    return None
        
def solvesudoku(board):
    # 1. search for empty cell
    blankpos = findblank(board)
    
    if not blankpos:
        return board 
    else:
        row,col = blankpos

    # 2.Iterate through guesses of num, if valid, call solvesudoku 
        for i in range(9): 
            if isvalid(i,blankpos,board)==True:
                board[row][col] = i 
                
                if solvesudoku(board):
                    return board
                
                board[row][col] = 0 
        return None 

#Testing 
def main(): 
    solved=[[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
    
    puzzle = [[0,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]]
    
    print(solvesudoku(puzzle))

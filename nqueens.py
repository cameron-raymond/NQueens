import random
import time

"""The n queens puzzle"""

class NQueens:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        print("Size:  "+str(size)+" initializing positions")
        self.totalConflicts = 0
        self.size = size
        self.positions = self.initializePositions(size)
        self.solve()
        print("Solved")

    def solve(self):
        i = 1
        while self.totalConflicts > 0:
            start = time.time()
            for column in range(len(self.positions)):
                if self.totalConflicts <= 0:
                    break
                row = self.positions[column]
                numConflicts = self.numConflicts(row,column,self.positions)
                rowToPut, minConflicts = self.minConflicts(column,self.positions)
                self.totalConflicts += (minConflicts-numConflicts)
                self.positions[column] = rowToPut
            end = time.time()
            print("Pass "+str(i)+" - duration: "+str(end - start)+", total number of conflicts " + str(self.totalConflicts))
            # self.show_full_board(self.positions)

            i+=1
        self.show_full_board(self.positions)
    
    def initializePositions(self,size):
        board = [None] * size
        for column in range(size):
            rowToPut, numConflicts = self.minConflicts(column,board) # See if we can put the queen along the diagonal
            board[column] = rowToPut
            self.totalConflicts += numConflicts
        return board

    def minConflicts(self,col,positions):
        minn = float('inf')
        bestRow = -1
        for row in range(len(positions)):
            conflicts = self.numConflicts(row, col, positions)
            # If moving a queen to a new row results in the same amount of conflicts, we'll do so 1 in n times (where n is the size of the chessboard )
            # this reduces the importance of the initial placings and helps avoid local minima
            if conflicts == minn:                       
                if random.randint(0,self.size) == 0: # Originally this was a random int between 0 and 1 but this meant that large chess boards would favour lower rows
                    minn = conflicts
                    bestRow = row
            if conflicts < minn:
                minn = conflicts
                bestRow = row
        return bestRow, minn

    # col is the column for the queen of interest
    # row is the potential new row to move the queen to
    def numConflicts(self, row, col, positions):
        total = 0
        queenPos = positions[col]
        for ind in range(len(positions)):
            if ind != col:
                otherQueen = positions[ind]
                if otherQueen == None:
                    return total
                elif row == otherQueen: # same row
                    total += 1
                elif row+col == otherQueen+ind: # same diag
                    total += 1
                elif row-col == otherQueen-ind: # same diag
                    total += 1
        return total

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[column] == row:
                    line += "Q "
                else:
                    line+=". "
            print(line)
        print("Total conflicts: "+str(self.totalConflicts))
        print("\n")

def readText(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content

if __name__ == '__main__':
    sizes = readText('./nqueens.txt')
    start = time.time()
    queen = NQueens(300)
    end = time.time()
    print("Time elapsed: "+str(end - start))
    
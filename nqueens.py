import random

"""The n queens puzzle"""


class NQueens:
    """Generate all valid solutions for the n queens puzzle"""

    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        self.totalConflicts = 0
        self.size = size
        self.positions = self.initializePositions(size)
        self.show_full_board(self.positions)
        self.solve()
        self.show_full_board(self.positions)

    def solve(self):
        i = 0
        while self.totalConflicts > 0:
            conflictsB = self.totalConflicts
            for column in range(len(self.positions)):
                if self.totalConflicts <= 0:
                    break
                row = self.positions[column]
                rowToPut, minConflicts, change = self.minConflicts(column,self.positions)
                # print("Moved queen in column "+str(column)+" from row "+str(row) + " to row " + str(rowToPut)+". Num conflicts: "+str(self.totalConflicts))
                self.totalConflicts += change
                self.positions[column] = rowToPut
            conflictsA = self.totalConflicts
            i+=1
            print("Pass "+str(i)+" went from "+str(conflictsB)+" conflicts to "+str(conflictsA)+". An improvement of "+str(conflictsB-conflictsA))
    
    def initializePositions(self,size):
        board = [None] * size
        for column in range(size):
            rowToPut, numConflicts = self.minConflicts(column,board) # See if we can put the queen along the diagonal
            board[column] = rowToPut
            self.totalConflicts += numConflicts
        return board

    def minConflicts(self,col,positions):
        """
            Takes in the column the queen is on, as well as the posititons of the queen's on the rest of the board,
            returns the best row the Queen can move to, the number of conflicts that the queen has moved into, and the difference in conflicts
            before and after the move
        """
        minn = float('inf')
        bestRow = -1
        beforeConflicts = None
        initRow = positions[col]
        for row in range(len(positions)):                
            conflicts = self.numConflicts(row, col, positions)
            if initRow != None and row == initRow:
                beforeConflicts = conflicts
            # If moving a queen to a new row results in the same amount of conflicts, we'll do so 1 in n times (where n is the size of the chessboard )
            # this reduces the importance of the initial placings and helps avoid local minima
            if conflicts == minn:                       
                if random.randint(0,self.size) == 0: # Originally this was a random int between 0 and 1 but this meant that large chess boards would favour lower rows
                    minn = conflicts
                    bestRow = row
            if conflicts < minn:
                minn = conflicts
                bestRow = row
        if beforeConflicts == None:
            return bestRow, minn
        changeInConflicts = (minn-beforeConflicts)
        return (bestRow, minn, changeInConflicts)

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
                elif row == otherQueen or row+col == otherQueen+ind or row-col == otherQueen-ind:  # if it's in the same row or diagnol, don't need to check columns because we only place on queen per column
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
    queen = NQueens(30)
    # for size in sizes:
    #     queen = NQueens(size)
    
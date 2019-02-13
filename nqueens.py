import random
import time
"""The n queens puzzle"""

class NQueens:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self, size, beta=False):
        # Store the puzzle (problem) size and the number of valid solutions
        self.totalConflicts = 0
        self.size = size
        self.beta = beta
        self.positions = self.initializePositions(size)
        # self.show_full_board(self.positions)
        self.solve()

    def solve(self):
        iteration = 0
        while self.totalConflicts > 0:
            conflictsB = self.totalConflicts
            for column in range(len(self.positions)):
                if self.totalConflicts <= 0:
                    break

                row = self.positions[column]
                rowToPut, minConflicts, change = self.minConflicts(column, self.positions)
                # print("Moved queen in column "+str(column)+" from row "+str(row) + " to row " + str(rowToPut)+". Num conflicts: "+str(self.totalConflicts))
                self.totalConflicts += change
                self.positions[column] = rowToPut
            conflictsA = self.totalConflicts

            iteration+=1
            improvement = conflictsB-conflictsA
            # print("Pass "+str(iteration)+" went from "+str(conflictsB)+" conflicts to "+str(conflictsA)+". An improvement of "+str(improvement))

        if self.totalConflicts > 0:
            print("Unable to solve problem")

    def initializePositions(self,size):
        board = [None] * size
        for column in range(size):
            rowToPut, numConflicts, _ = self.minConflicts(column,board) # See if we can put the queen along the diagonal
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
        initRow = positions[col]
        beforeConflicts = self.numConflicts(initRow, col, positions) if positions[col] is not None else float('inf')

        for row in range(len(positions)):
            conflicts = self.numConflicts(row, col, positions)

            # If moving a queen to a new row results in the same amount of conflicts, we'll do so 1 in n times (where n is the size of the chessboard )
            # this reduces the importance of the initial placings and helps avoid local minima

            if conflicts < minn:
                minn = conflicts
                bestRow = row

            elif conflicts == minn and (bestRow == initRow or random.randint(0, self.size) == 0): # Originally this was a random int between 0 and 1 but this meant that large chess boards would favour lower rows
                minn = conflicts
                bestRow = row

        changeInConflicts = (minn-beforeConflicts)
        return bestRow, minn, changeInConflicts

    # col is the column for the queen of interest
    # row is the potential new row to move the queen to
    def numConflicts(self, row, col, positions):
        total = 0
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


def test():
    timesShort = []
    timesMedium = []
    timesLong = []

    betaTimesShort = []
    betaTimesMedium = []
    betaTimesLong = []

    count = 0
    while count < 100:
        count+=1
        start = time.time()
        queen = NQueens(64)
        timesShort.append(time.time() - start)

        start = time.time()
        queen = NQueens(120)
        timesMedium.append(time.time() - start)
        start = time.time()
        queen = NQueens(150)
        timesLong.append(time.time() - start)

        start = time.time()
        queen = NQueens(64, True)
        betaTimesShort.append(time.time() - start)
        start = time.time()
        queen = NQueens(120, True)
        betaTimesMedium.append(time.time() - start)
        start = time.time()
        queen = NQueens(150, True)
        betaTimesLong.append(time.time() - start)

        print("---")
        print(sum(timesShort)/len(timesShort), "avg for timesShort")
        print(sum(timesMedium)/len(timesMedium), "avg for timesMedium")
        print(sum(timesLong)/len(timesLong), "avg for timesLong")
        print()
        print(sum(betaTimesShort)/len(betaTimesShort), "avg for betaTimesShort")
        print(sum(betaTimesMedium)/len(betaTimesMedium), "avg for betaTimesMedium")
        print(sum(betaTimesLong)/len(betaTimesLong), "avg for betaTimesLong")

if __name__ == '__main__':
    test()
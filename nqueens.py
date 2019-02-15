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

        # self.solve()

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

        candidates = []
        colCon = self.colConflicts(col, positions)
        for row in range(len(colCon)):
            rowCons = colCon[row]
            if rowCons > minn:
                pass
            elif rowCons < minn:
                minn = rowCons
                candidates = [row]
            else:
                candidates.append(row)
        choice = random.choice(candidates)
        beforeConflicts = colCon[initRow] if initRow is not None else float('inf')
        changeInConflicts = (minn-beforeConflicts)
        return choice, minn, changeInConflicts

    def colConflicts(self, col, positions):
        total = [0]*len(positions)
        for ind in range(len(positions)):
            if ind != col:
                otherQueen = positions[ind]
                if otherQueen != None:
                    total[otherQueen] += 1
                    diagonal = abs(col-ind)
                    if otherQueen+diagonal < len(positions):
                        total[otherQueen+diagonal] += 1
                    if otherQueen-diagonal >= 0:
                        total[otherQueen-diagonal] += 1
        return total

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
    initialConflictsSmall = []
    initialConflictsMed = []
    initialConflictsLarg = []

    count = 0
    while count < 100:
        count+=1
        print("STARTING PASS "+str(count))
        large = NQueens(1000000)
        initialConflictsLarg.append(large.totalConflicts)
        print("DONE PASS "+str(count))




    print("---")
    # print(sum(initialConflictsSmall)/len(initialConflictsSmall), "avg initial conflicts small")
    # print(sum(initialConflictsMed)/len(initialConflictsMed), "avg initial conflicts medium")
    print(sum(initialConflictsLarg)/len(initialConflictsLarg), "avg initial conflicts large")
    

if __name__ == '__main__':
    test()

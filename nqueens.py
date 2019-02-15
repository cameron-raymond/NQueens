import random
import time
from datetime import timedelta

"""The n queens puzzle"""

class NQueens:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self, size, beta=False):
        # Store the puzzle (problem) size and the number of valid solutions
        self.size = size
        self.beta = beta
        self.rowConflicts=[0]*size
        self.diag1Conflicts=[0]*(2*size-1)
        self.diag2Conflicts=[0]*(2*size-1)
        self.initializePositions()
        # self.show_full_board(self.positions)
        # Use this if you want to see a breakdown of which functions are taking the most time
        self.solve()

    def solve(self):
        maxIters = 100
        currentIter = 0
        success = False
        while currentIter < maxIters:
            column = self.findConflictingCol()
            if column < 0:
                success = True
                break
            row = self.positions[column]
            rowToPut, minConflicts = self.minConflicts(column)
                # print("Moved queen in column "+str(column)+" from row "+str(row) + " to row " + str(rowToPut)+". Num conflicts: "+str(self.totalConflicts))
            self.remove_queen(self.positions[column], column)
            self.add_queen(rowToPut, column)
            currentIter+=1

        if (not success):
            self.restart()

    def restart(self):
        self.rowConflicts=[0]*self.size
        self.diag1Conflicts=[0]*(2*self.size-1)
        self.diag2Conflicts=[0]*(2*self.size-1)
        self.initializePositions()
        self.solve()

    def findConflictingCol(self):
    	num_vars_violated = 0
    	vio_col = []
    	max_vios = 0
    	num_vios = 0
    	for col in range(0, self.size):
    		row=self.positions[col]
    		num_vios = self.rowConflict(row, col)
    		if 3 != num_vios: #three = zero violations
    			vio_col.append(col)
    	num_vars_violated = len(vio_col)
    	if num_vars_violated == 0:
    		return -1
    	return random.choice(vio_col)

    def initializePositions(self):
        self.positions = [None] * self.size
        for column in range(self.size):
            rowToPut, numConflicts = self.minConflicts(column) # See if we can put the queen along the diagonal
            self.add_queen(rowToPut, column)

    def add_queen(self, row, col):
        self.positions[col] = row
        self.rowConflicts[row] = self.rowConflicts[row]+1
        self.diag1Conflicts[(self.size-1)+(col-row)] = self.diag1Conflicts[(self.size-1)+(col-row)]+1
        self.diag2Conflicts[row+col] = self.diag2Conflicts[row+col]+1

    def remove_queen(self, row, col):
        self.positions[col] = 0
        self.rowConflicts[row] = self.rowConflicts[row]-1
        self.diag1Conflicts[(self.size-1)+(col-row)] = self.diag1Conflicts[(self.size-1)+(col-row)]-1
        self.diag2Conflicts[row+col] = self.diag2Conflicts[row+col]-1

    def minConflicts(self,col):
        """
            Takes in the column the queen is on, as well as the posititons of the queen's on the rest of the board,
            returns the best row the Queen can move to, the number of conflicts that the queen has moved into, and the difference in conflicts
            before and after the move
        """
        minn = float('inf')
        bestRow = -1
        initRow = self.positions[col]

        candidates = []
        for row in range(self.size):
            if row == initRow:
                continue
            rowCons = self.rowConflict(row, col)
            if rowCons > minn:
                pass
            elif rowCons < minn:
                minn = rowCons
                candidates = [row]
            else:
                candidates.append(row)
        choice = random.choice(candidates)
        return choice, minn

    def rowConflict(self, row, col):
         return self.rowConflicts[row]+self.diag1Conflicts[(self.size-1)+(col-row)]+self.diag2Conflicts[col+row]

    def colConflicts(self, col):
        total = [0]*self.size
        for ind in range(self.size):
            if ind != col:
                otherQueen = self.positions[ind]
                if otherQueen != None:
                    total[otherQueen] += 1 # Same row
                    d = abs(col-ind)
                    if otherQueen+d < self.size: # diagonal
                        total[otherQueen+d] += 1
                    if otherQueen-d >= 0: # other diagonal
                        total[otherQueen-d] += 1
        return total

    def show_full_board(self):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if self.positions[column] == row:
                    line += "Q "
                else:
                    line+=". "
            print(line)

def readText(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content



if __name__ == '__main__':
    sizes = readText('./nqueens.txt')
    for size in sizes:
        print("Starting Size: "+str(size))
        start = time.time()
        queen = NQueens(size)
        timeTaken = time.time()-start
        print("Finished Size: "+str(size)+"\n Time Taken: "+str(timedelta(seconds=timeTaken)))
        print("---")



def test():
    initialConflictsSmall = []
    initialConflictsMed = []
    timesLong = []

    count = 0
    while count < 10:
        # print(count)
        count+=1
        # start = time.time()
        # queen = NQueens(100)
        # timesShort.append(time.time() - start)

        # start = time.time()
        # queen = NQueens(120)
        # timesMedium.append(time.time() - start)
        start = time.time()
        queen = NQueens(20000)
        timeTaken = time.time()-start
        print("Pass: "+str(count)+", time taken: "+str(timeTaken))
        timesLong.append(time.time() - start)
        

        # start = time.time()
        # queen = NQueens(64, True)
        # betaTimesShort.append(time.time() - start)
        # start = time.time()
        # queen = NQueens(120, True)
        # betaTimesMedium.append(time.time() - start)
        # start = time.time()
        # queen = NQueens(20000, True)
        # betaTimesLong.append(time.time() - start)

    print("---")
    # print(sum(initialConflictsSmall)/len(initialConflictsSmall), "avg initial conflicts small")
    # print(sum(initialConflictsMed)/len(initialConflictsMed), "avg initial conflicts medium")
    print(sum(timesLong)/len(timesLong), "avg time large")
    
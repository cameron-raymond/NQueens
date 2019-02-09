import random
"""The n queens puzzle"""


class NQueens:
    """Generate all valid solutions for the n queens puzzle"""

    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        self.size = size
        self.positions = self.initializePositions(size)
        self.optimize()
        # self.showFullBoard(self.positions)
    
    def initializePositions(self,size):
        board = [None] * size
        for column in range(size):
            rowToPut = self.minConflicts(column,board) # See if we can put the queen along the diagonal
            board[column] = rowToPut
        return board

    def optimize(self):
        self.showFullBoard(self.positions)


    def minConflicts(self,column,positions):
        return random.randint(0,len(positions))
            
    
    def showFullBoard(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[column] == row:
                    line += "Q "
                else: 
                    line+=". "
            print(line)
        print("\n")


def readText(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content] 
    return content




if __name__ == '__main__':
    sizes = readText('./nqueens.txt')
    for size in sizes:
        queen = NQueens(size)


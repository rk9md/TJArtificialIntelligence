import sys
'''
This script takes in the string representation of a standard tic tac toe board 
as a command line argument and returns the possible moves for the player whose
turn it is. The script assumes the standard rules of tic tac toe 
(X moves first, first player to three in a row wins, players alternate turns, etc). 

The board is represented by a string of length 9 consisting of periods, X’s, and O’s.
The periods represent empty spaces, the X’s represent where the X player has placed their piece,
and the O represents where the O player has placed their piece. 
Each spot on the board is also referred to by its index which is given as follows:
0 1 2
3 4 5
6 7 8

The moves are categorized into good, bad, and tie. 
The “good” moves are the moves that lead to a win no matter what the opponent does. 
The “bad” moves are the moves that lead to a loss no matter what the opponent does. 
The “tie” moves are the rest of the moves (moves that could lead to either a win or a loss depending on the opponent). 

'''

# Number of rows/cols
side = 3
# Number of Total Spaces
n = side**2
# List of the sets of indexes of the spaces in each row, column, and diagonal. 
rowsColsDiags = [{0,1,2},{3,4,5}, {6,7,8}, {0,3,6},{1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]
# List of the list of indexes of the spaces in each row, column, and diagonal.
listRowsColsDiags = [[*x] for x in rowsColsDiags]
# The two possible symbols for the game of tic tac toe
sym = ["X", "O"]

# Checks if the string representation of the board is valid by 
# ensuring its length is 9 and by making sure that the board 
# either has the same number of X's and O's or has one more X.
# Returns 1 for a valid board and 0 for an invalid board.
def validBoard(pzl):
    return pzl.count("X")-pzl.count("O") in {1,0} and len(pzl)==n

# Determines whose turn turn it is. Odd number of periods means X turn
# and even means O turn. Returns 0 for X and 1 for O.    
def whoseTurn(pzl):
    return 1-pzl.count(".")&1

# Prints out the puzzle as a 3x3 square.
def display(pzl):
    [print(pzl[x:x+side]) for x in range(0,n,side)]

# Returns the index of the empty spaces on the board.
def emptySpaces(pzl):
    return [x for x in range(len(pzl)) if pzl[x]=="."]    

# Determines if a player won. Checks every row/column/diagonal if
# there is 3 of the same piece. Returns true if a player won, returns false otherwise.
def gameOver(pzl): 
    for x in listRowsColsDiags:
        if pzl[x[0]]==pzl[x[1]]==pzl[x[2]]!=".":
            return True
    return False

'''
Recursive method that determines the good, bad, and tie moves for a given board.
Two bases cases:
If a player has won, return a non empty bad set, so the previous recursion can categorize the move as good for the previous player.
If no one has won, return a non empty tie set, so the previous recursion can categorize the move as a tie move for the previous player.

Recursive Case:
Iterate through every possible move for the current player, create a new board as if the current player played at that spot, and recur
on the new board for the opposite player. 
If the recursion returns any moves that guarantee a win for the opponent, add the move the player hypothetically made into the bad category. 
If the recursion returns any moves that cannot guarantee a win or a loss for the opponent, add the move the player hypothetically made into the tie category. 
If the recursion returns any moves that guarantee a loss for the opponent, add the move the player hypothetically made into the good category. 
'''
def partitionMoves(pzl, turn, numSpaces):
    if gameOver(pzl):
        return set(),{""},set()
    if numSpaces==0:
        return set(),set(),{""}
    good,bad,tie = set(),set(),set()
    for x in emptySpaces(pzl):
        newPzl = pzl[:x]+sym[turn]+pzl[x+1:]
        tempGood, tempBad, tempTie = partitionMoves(newPzl,1-turn, numSpaces-1)
        if tempGood:
            bad.add(x)
        elif tempTie:
            tie.add(x)
        else:
            good.add(x)
    return good, bad, tie    

# Read in the commmand line parameter of the board.
pzl = sys.argv[1].upper()
display(pzl)
# Check if the board is valid or one player has already won.
# If no one has won, the board is valid, and the game is not tied, run partitionMoves to find out the set of moves for the given board.
if not validBoard(pzl):
    print("Invalid Starting Board")
elif gameOver(pzl):
    print("Game has already finished")
else:
    who = whoseTurn(pzl)
    empty = len(emptySpaces(pzl))
    if empty == 0:
        print("Game has already finished in a tie.")
    else:
        g,b,t = partitionMoves(pzl, who, empty)
        if not g:
            g = " None "
        if not b:
            b = " None "
        if not t:
            t = " None "
        print("Good moves: "+str(g)[1:-1])
        print("Bad moves: "+str(b)[1:-1])
        print("Tie moves: "+str(t)[1:-1])
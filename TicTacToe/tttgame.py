import sys, time, msvcrt
'''
This script will play out a human vs computer game of tic tac toe. Optional Command line arguments are the starting board and the piece the human will be. 
The script assumes the standard rules of tic tac toe (X moves first, first player to three in a row wins, players alternate turns, etc). 

The board is represented by a string of length 9 consisting of periods, X’s, and O’s.
The periods represent empty spaces, the X’s represent where the X player has placed their piece,
and the O represents where the O player has placed their piece. 
Each spot on the board is also referred to by its index which is given as follows:
0 1 2
3 4 5
6 7 8
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

# Returns a list of the index of the empty spaces on the board.
def emptySpaces(pzl):
    return [x for x in range(len(pzl)) if pzl[x]=="."] 
# Returns a list of the index of the empty spaces on the board as a string.  
def emptySpacesStr(pzl):
    return [str(x) for x in range(len(pzl)) if pzl[x]=="."]

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


# Returns the index of the best move possible for the given player and the given board.
# Returns -1 for the an invalid board
# Returns 10 for a finished game.
def nextMove(pzl, who):
    if not validBoard(pzl):
        print("Invalid Board")
        return -1
    elif gameOver(pzl):
        print("Game is already finished")
        return 10
    else:
        g,b,t = partitionMoves(pzl, who, len(emptySpaces(pzl)))
        for x in [g,t,b]:
            if x:
                return x.pop()


# Takes in up to two command line arguments. 
# The single character argument is set to the human's piece
# The multicharacter argument is read in as the starting board for the game.
# These arguments can be read in any order.
# If no board is given, the default is the empty board.
# If no human character is given, teh default is setting the computer to the player with the next move and the human to the other. 
pzl = None
human = None
argCount = 0
for x in sys.argv[1:]:
    if len(x)==1:
        x = x.upper()
        if x == "X":
            human = 0
        else:
            human = 1
        comp = 1-human
    else:
        pzl = x.upper()
    argCount+=1
    if argCount==2:
        break

if not pzl:
    pzl= "........."
if human==None:
    comp = whoseTurn(pzl)
    human = 1-comp


'''
This code plays out a game of tic tac toe given the parameters in the command line. The human is asked for their turn and is expected to type the index of where they want to play.
The computer will make its move automatically in response to the human. The current board will display after each move as well as the move the active player made. If the human
plays an invalid move, then they will be reprompted until a correct move is given or the player's time is up.

Once the game is finished, the script will print out the outcome of the game.
'''
turn = whoseTurn(pzl)
if validBoard(pzl):
    if not gameOver(pzl):
        while True:
            display(pzl)
            print()
            placement = 0
            if turn==human:
                print("Your Move:",end=" ", flush=True)
                timeout = 60
                startTime = time.time()
                poss = emptySpacesStr(pzl)
                
                while True:
                    if msvcrt.kbhit():
                        inp = msvcrt.getch()
                        inp = str(inp)
                        placement = inp[2]
                        if placement in poss:
                            placement =int(placement)
                            print(placement)
                            break
                        else:
                            print("\nInvalid. Try another spot. Move:", end=" ", flush=True)
                    elif time.time() - startTime > timeout:
                        placement = nextMove(pzl, turn)
                        print(placement)
                        print("Time up! Automatically assigning player's move")
                        break
            else:
                print("Computer's move:", end=" ", flush=True)
                placement = nextMove(pzl,turn)
                print(placement)
            pzl = pzl[:placement]+sym[turn]+pzl[placement+1:]
            if gameOver(pzl):
                display(pzl)
                print(sym[turn]+" has won the game!")
                break
            if "." not in pzl:
                display(pzl)
                print("The game ends in a tie!")
                break
            turn = 1-turn
    else:
        print("Game already finished")
else:
    print("Invalid board entered")

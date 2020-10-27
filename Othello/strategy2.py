import sys, time, random 
class Strategy:
    def best_strategy(self, board, player, best_move, still_running):
        s=8
        n=s*s
        colors = ["X","O"] #O=White X=Black
        num = {str(x) for x in range(64)}
        aStr = "ABCDEFGH" 
        alphaDict = {z:aStr.index(z) for z in aStr}
        alpha = set(aStr)
        numToRow = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 3, 25: 3, 26: 3, 27: 3, 28: 3, 29: 3, 30: 3, 31: 3, 32: 4, 33: 4, 34: 4, 35: 4, 36: 4, 37: 4, 38: 4, 39: 4, 40: 5, 41: 5, 42: 5, 43: 5, 44:5, 45: 5, 46: 5, 47: 5, 48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 6, 54: 6, 55: 6, 56: 7, 57: 7, 58: 7,59: 7, 60: 7, 61: 7, 62: 7, 63: 7}
        numToCol = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7, 16: 0, 17: 1, 18: 2, 19: 3, 20: 4, 21: 5, 22: 6, 23: 7, 24: 0, 25: 1, 26: 2, 27: 3, 28: 4, 29: 5, 30: 6, 31: 7, 32: 0, 33: 1, 34: 2, 35: 3, 36: 4, 37: 5, 38: 6, 39: 7, 40: 0, 41: 1, 42: 2, 43: 3, 44:4, 45: 5, 46: 6, 47: 7, 48: 0, 49: 1, 50: 2, 51: 3, 52: 4, 53: 5, 54: 6, 55: 7, 56: 0, 57: 1, 58: 2,59: 3, 60: 4, 61: 5, 62: 6, 63: 7}

        # def boardChange(pzl):
        #     final = ""
        #     for x in range(8):
        #         final+=pzl[11+x*8,19+x*8]
        #     return final

        def alphaToNum(pos):
            return (int(pos[1])-1)*8+alphaDict[pos[0]]

        def numToAlpha(pos):
            number = pos//8+1
            letter = aStr[pos%8]
            return letter+str(number)

        def whoseTurn(pzl):
            return (len(white)+len(black))&1

        def display(pzl):
            [print(pzl[x:x+s]) for x in range(0,n,s)]
            print()

        pzl, color = board, player

        tournament = False
        #white = {x for x in range(64) if pzl[x]=="O"}
        #black = {x for x in range(64) if pzl[x]=="X"}
        if len(pzl)!=64:
            tournament = True
            pzl = "".join(pzl)
            pzl = pzl.replace("?", "")
            pzl = pzl.replace("@", "X")
            pzl = pzl.upper()
        if color == "@":
            color = "X"
        color = color.upper()
        # print(pzl, color)
        opp = ({*colors}-{color}).pop()
        white = {x for x in range(64) if pzl[x]=="O"}
        black = {x for x in range(64) if pzl[x]=="X"}
        colorDict = {"O":white, "X":black}
        oppSet = colorDict[opp]

        
        direction = [1,-1,-8,8,-7,-9,9,7]
        changes = {1:(0,1), -1:(0,-1), -8:(-1,0), 8:(1,0), -7:(-1, 1), -9:(-1,-1), 9:(1, 1), 7:(1, -1)}
        #coord = {x:(numToRow[x], numToCol[x]) for x in range(64)}

        def inBounds(val, direction, row, col):
            if val>-1 and val<64:
                valR = numToRow[val]
                valC = numToCol[val]
                return valR==row and valC==col
            return False

        def legalMoves(pzl, colorMove, black, white):
            moves = {}
            colorDict = {"O":white, "X":black}
            opp = dictEnemy[colorMove]
            for x in colorDict[colorMove]:
                tempx = x
                xrow = numToRow[x]
                xcol = numToCol[x]
                for z in direction:
                    x = tempx
                    expectedRow = xrow
                    expectedCol = xcol
                    path = set()
                    tup = changes[z]
                    expectedRow += tup[0]
                    expectedCol += tup[1]
                    if inBounds(x+z, direction, expectedRow, expectedCol):
                        if pzl[x+z]==opp:
                            x+=z
                            expectedRow += tup[0]
                            expectedCol += tup[1]
                            while pzl[x]==opp and inBounds(x+z, direction, expectedRow, expectedCol):
                                path.add(x)
                                x+=z
                                expectedRow += tup[0]
                                expectedCol += tup[1]
                            if pzl[x]==".":
                                if x not in moves:
                                    moves[x] = set()
                                moves[x] = moves[x].union(path)
            return moves

        def flipper(npzl, changeSet, ncolor, pos):
            for r in changeSet:
                z = npzl[r]
                npzl  = npzl[:r]+ncolor+npzl[r+1:]
            npzl  = npzl[:pos]+ncolor+npzl[pos+1:]
            return npzl

        def bestMove(pzl, color, black, white):
            maxi = 0
            maxPos = None
            safeedges = set()
            innersquares =  []
            if legal:
                if len(legal)==1:
                    return list(legal)[0]
                for x in legal:
                    alpha = numToAlpha(x)
                    val = len(legal[x])
                    if alpha not in evilSet:
                        # if alpha in {"H8", "H1", "A8", "A1"}:
                        #     corners.add(x)
                        if len({"H", "A", "8", "1"}|set(alpha))==5:
                            #print("Ajith")
                            postpzl = pzl
                            for r in legal[x]:
                                postpzl  = postpzl[:r]+color+postpzl[r+1:]
                            passed = [True, True]
                            newx = x
                            if alpha[0] in {"H", "A"}:
                                while newx!=63 and newx!=56:
                                    if postpzl[newx]!=color:
                                        passed[0] = False
                                        break
                                    newx+=8
                                newx = x
                                while newx!=0 and newx!=7:
                                    if postpzl[newx]!=color:
                                        passed[0] = False
                                        break
                                    newx-=8
                                newx = x
                            if alpha[1] in {"8", "1"}:
                                newx = x
                                while newx!=7 and newx!=63:
                                    if postpzl[newx]!=color:
                                        passed[1] = False
                                        break
                                    newx+=1
                                newx = x
                                while newx!=0 and newx!=56:
                                    if postpzl[newx]!=color:
                                        passed[1] = False
                                        break
                                    newx-=1
                            if passed[0] or passed[1]:
                                safeedges.add(x)
                        elif val>maxi:
                            maxi = val
                            innersquares.clear()
                            innersquares.append(x)
                            maxPos = x
                        elif val==maxi:
                            #maxi = val
                            innersquares.append(x)
                            #maxPos = x
                    
            
            if safeedges:
                return random.choice([*safeedges])
            elif innersquares:
                return innersquares[0]
            else:
                for x in legal:
                    alpha = numToAlpha(x)
                    if alpha not in evilSet:
                        return x
                    if pzl[alphaToNum(evilDict[alpha])]==color:
                        return x
            return list(legal)[random.randint(0, len(legal)-1)]
        def boardEval(pzl, token):
            periods = 0
            mine = 0
            for x in pzl:
                if x ==token:
                    mine+=1
                if x == ".":
                    periods+=1
            return mine - (64-periods-mine)
        dictEnemy = {'X':"O", "O":"X"}
        tokentoNum = {'X':0, "O":1}
        def negaMax(pzl, token, depth, black, white, passes):
            if depth == 0 or passes==2 or len(black)+len(white)==64:
                if token=="X":
                    return [len(black)-len(white)]
                else: 
                    return [len(white)-len(black)]
            lm = legalMoves(pzl, token, black, white)
            #print(lm)
            if not lm:
                nm = negaMax(pzl, dictEnemy[token], depth -1, black, white, passes+1)
                return [-1*nm[0]]+nm[1:]+[-1]
            if token=="X":
                nmlist = sorted([negaMax(flipper(pzl, lm[pos], token, pos), dictEnemy[token], depth-1,  {*black,*lm[pos],pos}, white-lm[pos], 0)+[pos] for pos in lm])
            else:
                nmlist = sorted([negaMax(flipper(pzl, lm[pos], token, pos), dictEnemy[token], depth-1,  black-lm[pos], {*white,*lm[pos],pos}, 0)+[pos] for pos in lm])
            best  = nmlist[0]
            return [-1*best[0]] + nmlist[0][1:]

        evilSet = {"B7", "B8", "A7", "B1", "A2", "B2", "G2", "G1", "H2", "G8", "G7", "H7"}
        evilSet = {"B7", "B8", "A7", "B1", "A2", "B2", "G2", "G1", "H2", "G8", "G7", "H7"}
        evilList = [*evilSet]
        corners = ["A8", "A1", "H1", "H8"]
        evilDict = {evilList[x]:corners[x//3] for x in range(len(evilList))}


        movesFromEnd = 8
        cornerset = {0, 7, 56, 63}
        display(pzl)
        legal = legalMoves(pzl, color, black, white)
        print("Legal moves: {}".format(set(legal)))
        cor = set(legal)&cornerset
        if cor:
            bestChoice = random.choice(list(cor))
            print("My heuristic choice is {}".format(random.choice(list(cor))))  
        else:
            bestChoice = bestMove(pzl, color, black, white)
            print("My heuristic choice is {}".format(bestChoice))
        newbestChoice = 11+(bestChoice//8)*10+(bestChoice%8)
        #print(bestChoice)
        if tournament:
            best_move.value = newbestChoice
        if (len(black)+len(white))>=(64-movesFromEnd):
            nm = negaMax(pzl, color, -1, black, white, 0)
            print("My negamax score is {} and my negamax choice is {}".format(nm, nm[-1]))
            bestChoice = nm[-1]
        
            #print("My heuristic choice is {}".format(bestChoice))
        #print(len(black)+len(white))
        
            #print("My negamax score is {} and my negamax choice is {}".format(bestChoice[0], bestChoice[-1]))
            #print(bestChoice)
        #print(bestChoice)
        preConvBC = bestChoice
        bestChoice = 11+(bestChoice//8)*10+(bestChoice%8)
        #print(bestChoice)
        if tournament:
            best_move.value = bestChoice
        else:
            return preConvBC
        #print(bestChoice)
# b = "???????????........??........??........??...o@...??...@o...??........??........??........???????????"
# p = "@"
# best_move = -1
# print(Strategy.best_strategy("Strategy", b, p, best_move, True))
# print(best_move)
if __name__ == "__main__":
    colors = ["X","O"]
    pzl2, color2= None, None
    for x in sys.argv[1:]:
        if len(x)==1:
            color2 = x
        else:
            pzl2 = x
    if not pzl2:
        pzl2 = "...........................OX......XO..........................."
    white = {x for x in range(64) if pzl2[x]=="O"}
    black = {x for x in range(64) if pzl2[x]=="X"}



    pzl2 = pzl2.upper()

    color2 = color2.upper()
    bc = 0
    bc = Strategy.best_strategy("Strategy", pzl2, color2, bc, True)
    #print(bc)
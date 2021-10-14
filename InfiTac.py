import re
# Säg till om du har något du tycker borde ändras


# Måste göras, kan finnas mer:

#   Turnstate

#   Main

#   User Input

#   AI

#region Statiska variabler
# hasattr() kollar om funktionen är initierad eller inte när den används. Om inte så sätts värdet till ett standardvärde.

def player1Tile(tile = None):   # KLAART

    if tile != None:
        player1Tile.savedTile = tile
    elif not hasattr(player1Tile, "savedTile"):
        player1Tile.savedTile = "x"

    return player1Tile.savedTile


def player2Tile(tile = None):   # KLAART

    if tile != None: 
        player2Tile.savedTile = tile
    elif not hasattr(player2Tile, "savedTile"):
        player2Tile.savedTile = "o"

    return player2Tile.savedTile

def winLength(board, num = None):   # KLAART

    if num != None:
        winLength.savedNum = num
        if winLength.savedNum > len(board): 
            winLength.savedNum = len(board)

    elif not hasattr(winLength, "savedNum"):
        winLength.savedNum = 3
        if winLength.savedNum > len(board): 
            winLength.savedNum = len(board)
    return winLength.savedNum


def emptyBoardTile(tile = None):
    if tile != None:
        emptyBoardTile.savedTile = tile
    elif not hasattr(emptyBoardTile, "savedTile"):
        emptyBoardTile.savedTile = "_"

    return emptyBoardTile.savedTile

#endregion

def saveBoard(board: list, currentPlayer, saveName: str):
    open(saveName+".txt", "w").close()
    save = open(saveName+".txt", "w")
    save.write(f"BoardSize: {len(board)}")
    for i in range(len(board)):
        boardRow = "".join([_ for _ in board[i]])
        save.write(boardRow)
    

    save.write(f"CurrentPlayer: {currentPlayer}")
    save.write(f"Player2: {player2Tile() if currentPlayer == player1Tile() else player1Tile()}")
    save.write(f"EmptyTile: {emptyBoardTile()}")
    save.close()
    pass

def loadBoard(saveName: str):
    save = open(saveName+".txt", "r")
    line = save.readline()
    boardSize = int(line.split("BoardSize: ")[1])

    board = []
    for i in range(boardSize):
        board[i] = save.readline().split()

    player1Tile(line.split("CurrentPlayer: ")[1])
    player2Tile(line.split("Player2: ")[1])
    emptyBoardTile(line.split("EmptyTile: ")[1])
    return board
    

def createBoard(size: int): # KLAART

    board = [[emptyBoardTile()]*size]*size
    return board


def viewBoard(board: list): # KLAART

    for i in range(len(board)):
        boardRow = ""
        for j in range(len(board[i])):
            boardRow += board[i][j]

        print(boardRow)
    pass


# Typ om man vill restarta eller nåt

def menu(title: str, prompt: str, options: dict): # KLAART 
    print(title)

    for k, v in options.items():
        print(f"{k}) {v}")

    print()

    userSelection = None

    while True:
        userSelection = input(prompt)
        if userSelection in options:
            break
    print()

    return userSelection

def boardState(board: list, newInput: list , playerTile: str): # Klar
    board[newInput[0]][newInput[1]] = playerTile
    viewBoard(board)
    gameOver = winCon(board, newInput, playerTile)

    if gameOver == True:
        print(f"Player {playerTile} won!")
    elif gameOver == None:
        print("It's a tie!")
        gameOver = True
    
    return not gameOver

def winCon(board: list, newInput: list, playerTile: str): # KLAAR den gör nåt
    pattern = re.compile(f"{playerTile*winLength(board)}")
    boardRow = "".join([_ for _ in board[newInput[1]]])
    boardColumn = "".join(board[:][newInput[0]])
    if pattern.search(boardRow) or pattern.search(boardColumn):
        return True

    direction = [] #diagonal1, går upp mot höger
    i = 0
    while newInput[1]+i < len(board) and newInput[0]+i < len(board): 
        if board[newInput[0]+i][newInput[1]+i] == playerTile:
            direction.append(1)
            i = i + 1
        else:
            break
    i = 1
    while newInput[1]-i >= 0 and newInput[0]-i >= 0: 
        if board[newInput[0]-i][newInput[1]-i] == playerTile:
            direction.append(1)
            i = i + 1
        else:
            break
    if sum(direction) >= 3: # 3 ger tictactoe, öka för större plan.
        return True
    direction = [] #diagonal1, går ner mot höger
    i = 0
    while newInput[1]-i >= 0 and newInput[0] +i< len(board): 
        if board[newInput[0]+i][newInput[1]-i] == playerTile:
            direction.append(1)
            i = i + 1
        else:
            break
    i = 1
    while newInput[0]-i >= 0 and newInput[1] +i < len(board): 
        if board[newInput[0]-i][newInput[1]+i] == playerTile:
            direction.append(1)
            i = i + 1
        else:
            break
    if sum(direction) >= 3: # 3 ger tictactoe, öka för större plan. 
        return True

    tie = ""
    for i in range(0,len(board)):
        if emptyBoardTile() in board[i]:
            tie = None
    if tie == None:
        return None

    return False

main()
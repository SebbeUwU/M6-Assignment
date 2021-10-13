from re import *



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

def createBoard(size: int, tile = emptyBoardTile()): # KLAART

    board = [[tile]*size]*size
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


def boardState(board: list, newInput: list , playerTile: str): # NOT DONE

    # newInput är på formen [x,y] för enkelhetens skull


    #typ sätt in ny tile som spelaren sa och sen kolla i alla riktningar för möjliga matchningar med regex eller nåt och rowCount()

    board[newInput[0]][newInput[1]] = playerTile

    pass








def winCon(board: list, newInput: list, playerTile: str):
    pattern = compile(f"{playerTile*winLength(board)}")
    boardRow = "".join([_ for _ in board[newInput[1]]])
    boardColumn = board[:][newInput[0]]
    if pattern.search(boardRow) or pattern.search(boardColumn):
        #Win
        pass



    
pass

emptyBoardTile()
board = createBoard(4)

winCon(board, [1,2], "_")
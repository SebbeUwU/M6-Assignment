import re
import os

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
    with open(saveName+".txt", "w") as save:
        save.write(f"BoardSize: {len(board)}\n")
        for i in range(len(board)):
            boardRow = " ".join([_ for _ in board[i]])
            save.write(boardRow + "\n")
    
        save.write(f"CurrentPlayer: {currentPlayer}\n")
        save.write(f"Player2: {player2Tile() if currentPlayer == player1Tile() else player1Tile()}\n")
        save.write(f"EmptyTile: {emptyBoardTile()}\n")
    pass

def loadBoard(saveName: str):
    board = []
    with open(saveName+".txt", "r") as save:
        boardSize = int(save.readline().split("BoardSize: ")[1])

        for i in range(boardSize):
            boardRow = save.readline()
            boardRow = boardRow[0:-1]
            boardRow = boardRow.split(" ")
            board.append(boardRow)

        player1Tile(save.readline().split("CurrentPlayer: ")[1][0:-1])
        player2Tile(save.readline().split("Player2: ")[1][0:-1])
        emptyBoardTile(save.readline().split("EmptyTile: ")[1][0:-1])

    return board
    

def createBoard(size: int): # KLAAR
    board = []
    for i in range(size):
        columns = []
        for j in range(size):
            columns.append(emptyBoardTile())
        board.append(columns)
    
    print(board)
   # board = [[emptyBoardTile()]*size]*size
    #board = [board[:] for i in range(size)]
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

def winCon(board: list, newInput: list, playerTile: str): # KLAAR den gör nåt
    pattern = re.compile(f"{playerTile*winLength(board)}")
    boardRow = "".join([_ for _ in board[newInput[1]]])
    boardColumn = "".join([row[newInput[0]] for row in board])
    
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
            continue
        else: return None

    return False


def play(startBoard, boardName="LastGame"):
    currentPlayer = player2Tile()
    board = startBoard
    gameOver = False
    while not gameOver:
        if currentPlayer == player1Tile():
            currentPlayer = player2Tile()
        else:
            currentPlayer = player1Tile()

        print(f"Player {currentPlayer}'s turn\n")
        viewBoard(board)
        print()

        saveBoard(board, currentPlayer, boardName)

        while True:
            userInput = input("x, y: ")
            
            try:
                emptyTile = True
                userInput = userInput.split(", ")
                userInputList = [int(userInput[0]), int(userInput[1])]
                x = userInputList[0]
                y = userInputList[1]

                if board[y][x] != "_":
                    raise TypeError

                break
                
            except ValueError:
                #redo
                print("Incorrect format, it needs to be as 'x, y'")
                continue
            except TypeError:
                print("Tile is occupied")
                continue
            except IndexError:
                print("Out of range")
                continue
        
        print()
        board[y][x] = currentPlayer
        gameOver = winCon(board, userInputList, currentPlayer) 

    if gameOver == True:
        print(f"Player {currentPlayer} won!\n")
    elif gameOver == None:
        print("It's a tie!\n")
        gameOver = True

    viewBoard(board)
    print()

    pass
        
def main():
    menuItems = {"p":"Play TicTacToe", "c":"Custom Game", "l":"Load Game", "q":"Quit"}
    while True:
        option = menu("Welcome to InfiniTac, what would you like to do\n", "Option: ", menuItems)
        if option == "p":
            player1Tile("x")
            player2Tile("o")
            board = createBoard(3)
            winLength(board, 3)
            play(board)
        elif option == "c":
            player1Tile(input("Choose a tile for player 1: "))
            player2Tile(input("Choose a tile for player 2: "))
            board = createBoard(int(input("Choose a boardsize: ")))
            winLength(board, int(input("Choose amount of tiles in a row to win: ")))
            saveName = input("Choose name of save: ")
            play(board, saveName)
            
        elif option == "l":
            print("Existing saves or input b to go back:")
            files = [f for f in os.listdir('.') if os.path.isfile(f)]

            [print(e[0:-4]) for e in files if ".txt" in e]
        
            saveName = input("\nPick save to continue: ")

            if saveName == "b":
                continue
            board = loadBoard(saveName)
            play(board, saveName)

        elif option == "q":
            print("Thank you for playing")
            break

main()
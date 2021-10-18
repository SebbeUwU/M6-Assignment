def win(board, choice, player):  #choice är det senaste lagda draget, player är symbolden på brädet som används.
    direction = [] #Koden är olik för alla riktningar, vet inte om det går att göra bättre
    i = 0          #Men känns som att det KANSKE går att få in det i 2 while loopar om man e smart
    while choice[1]+i < len(board): #En test att "i" tillsammans med choice är inom brädspelet
        if board[choice[0]][choice[1]+i] == player: #Först tittar programmet åt höger om punkten choice,. så länge punkten på board == player läggs en till 1 i direction
            direction.append(1)
            i = i + 1
        else:
            break
    i = 1
    while choice[1]-i >= 0: #Sen åt vänster om punkten choice
        if board[choice[0]][choice[1]-i] == player:
            direction.append(1)
            i = i + 1
        else:
            break
    if sum(direction) >= 3: # 3 ger tictactoe, öka för större plan.
        return True
        #repetera det här för alla riktningar
    direction = [] #vertical
    i = 0
    while choice[0]+i < len(board): 
        if board[choice[0]+i][choice[1]] == player:
            direction.append(1)
            i = i + 1
        else:
            break
    i = 1
    while choice[0]-i >= 0: 
        if board[choice[0]-i][choice[1]] == player:
            direction.append(1)
            i = i + 1
        else:
            break
    if sum(direction) >= 3: # 3 ger tictactoe, öka för större plan.
        return True
    direction = [] #diagonal1, går upp mot höger
    i = 0
    while choice[1]+i < len(board) and choice[0]+i < len(board): 
        if board[choice[0]+i][choice[1]+i] == player:
            direction.append(1)
            i = i + 1
        else:
            break
    i = 1
    while choice[1]-i >= 0 and choice[0]-i >= 0: 
        if board[choice[0]-i][choice[1]-i] == player:
            direction.append(1)
            i = i + 1
        else:
            break
    if sum(direction) >= 3: # 3 ger tictactoe, öka för större plan.
        return True
    direction = [] #diagonal1, går ner mot höger
    i = 0
    while choice[1]-i >= 0 and choice[0] +i< len(board): 
        if board[choice[0]+i][choice[1]-i] == player:
            direction.append(1)
            i = i + 1
        else:
            break
    i = 1
    while choice[0]-i >= 0 and choice[1] +i < len(board): 
        if board[choice[0]-i][choice[1]+i] == player:
            direction.append(1)
            i = i + 1
        else:
            break
    if sum(direction) >= 3: # 3 ger tictactoe, öka för större plan. 
        return True
    return False

def play(board = createBoard(3)):
    currentPlayer = player1Tile()
    gameOver = True
    while gameOver:
        while True:
            userInput = input("x, y: ")
            try: 
                userInput = userInput.split(", ")
                userInputList = [int(userInput[0]), int(userInput[1])]
                print(userInputList)
                break
            except ValueError:
                #redo
                print("Incorrect format, it needs to be as 'x, y'")
                continue
        gameOver = boardState(board, userInputList, currentPlayer)
        if currentPlayer == player1Tile():
            currentPlayer = player2Tile()
        else:
            currentPlayer = player1Tile()
    pass
        
def main():
    menuItems = {"p":"Play TicTacToe", "c":"Custom Game", "l":"Load Game", "q":"Quit"}
    while True:
        option = menu("Welcome to InfiniTac, what would you like to do", "Option: ", menuItems)
        if option == "p":
            play()
        elif option == "c":
            player1Tile(int(input("Choose a tile for player 1: ")))
            player2Tile(int(input("Choose a tile for player 2: ")))
            board = createBoard(int(input("Choose a boardsize: ")))
            winLength(int(input("Choose amount of tiles in a row to win: ")))
            play(board)
            
        elif option == "l":
            
            play(board)
        elif option == "q":
            print("Thank you for playing")
            break

def win(board, choice, player):  #choice är det senaste lagda draget, player är symbolden på brädet som används
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

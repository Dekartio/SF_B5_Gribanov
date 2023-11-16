board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
Player = "X"
winner = None
gameplay = True



def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    vvod = int(input("Введите номер от 1 до 9: "))
    if vvod >= 1 and vvod <= 9 and board[vvod-1] == "-":
        board [vvod-1]=Player
    else:
        print("Место занято!")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner  = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameplay
    if "-" not in board:
        printBoard(board)
        print("Ничья! ")
        gameplay = False

def checkWin(board):
    if checkHorizontal(board) or checkDia(board) or checkRow(board):
        print(f"Побеждает {winner}")

def switch():
    global Player
    if Player == "X":
        Player = "O"
    else:
        Player = "X"

while gameplay:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switch()


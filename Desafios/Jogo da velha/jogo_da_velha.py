blank = " "
token = ["X","O"]

def criarboard():
    board = [
        [blank, blank, blank],
        [blank, blank, blank],
        [blank, blank, blank],
    ]
    return board

def printBoard(board):
    for i in range(3):
        print("|".join (board[i]))
        print("------")

def movimentos (mensagem):
    try:
       n = int(input(mensagem))
       if n<=3 and n>=1:
           return n -1
       else:
           print("Numero precisa estar entre 1 e 3")
           return movimentos
    except:
        print("Numero não é valido")
        movimentos(mensagem)

def verifica_movimento(board, i, j):
    if board[i][j] == blank:
        return True
    else:
        return False

def faz_movimento(board, i, j, player):
    board[i][j] = token[player]

def verificar_ganhador(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != blank:
            return board[i][0]
        
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != blank:
            return board[0][i]
        
    if board[0][i] != blank and board [0][0] == board [1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][i] != blank and board [0][2] == board [1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == blank:
                return False

    return "EMPATE"
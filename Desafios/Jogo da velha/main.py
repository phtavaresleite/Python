from jogo_da_velha import criarboard, movimentos, verificar_ganhador, printBoard, verifica_movimento, faz_movimento

player = 0
board = criarboard()
ganhador = verificar_ganhador(board)

while(not ganhador):
    printBoard(board)
    
    i = movimentos("Digite a linha: ")
    j = movimentos("Digite a coluna: ")

    if verifica_movimento(board, i,j):
        faz_movimento(board, i,j, player)
        ganhador = verificar_ganhador(board)
        player = (player + 1) %2
    else:
        print("A posição informada já está ocupada")
        

print("Ganhador foi ",ganhador)
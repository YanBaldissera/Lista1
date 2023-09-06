""" Para fazer a montagem utilizei os mesmo conceitos do jogo anterior a diferença foi que nesse foi utilizado parametros tanto na 
função de criar o tabuleiro quanto na verificação da vitoria."""




def criarTabuleiro(valor):
    """ Vai retornar o tabuleiro """
    tabuleiro = [[" " for _ in range(valor)] for _ in range(valor)]
    return tabuleiro
    
        
def tabuleiro(tabuleiro):
    "vai imprimir o tabuleiro no formato"
    for linha in tabuleiro:
        print("  |  ".join(linha))
        print("-" * 100)
    

def verificarVitoria(tabuleiro, jogador, valor):
    """ Vai retornar se já houve algum ganhador ou não """
    for linhas in tabuleiro:
        if all(posicao == jogador for posicao in linhas):
            return True
    
    for colunas in range(valor):
        colunaAtual = [tabuleiro[linhas][colunas] for linhas in range(valor)]
        
        if all(posicao == jogador for posicao in colunaAtual):
            return True
        
    
    diagonalPrimaria = [tabuleiro[i][i] for i in range(valor)]
    if all(posicao == jogador for posicao in diagonalPrimaria):
        return True
    
    diagonalSecundaria = [tabuleiro[i][3 - i] for i in range(valor)]
    if all(posicao == jogador for posicao in diagonalSecundaria):
        return True
    
    
    return False



def jogoDaVelha():
    """ Vai retornar o jogo """
    
    valor = int(input("Entre com o valor do tamanho do jogo da velha: "))
    jogo = criarTabuleiro(valor)
    
    jogadorAtual = "X"
    
    while True:
        tabuleiro(jogo)
        
        print(f"Jogador {jogadorAtual}, é a sua vez.")
        linha = int(input(f"Digite o número da linha (0-{valor - 1})"))    
        coluna = int(input(f"Digite o número da coluna (0-{valor - 1})"))
        
        if 0 <= linha < valor and 0 <= coluna < valor and jogo[linha][coluna] == " ":
            jogo[linha][coluna] = jogadorAtual
            
            if verificarVitoria(jogo, jogadorAtual, valor):
                tabuleiro(jogo)
                print(f"Jogador {jogadorAtual} venceu!!!")
                break
            else:
               jogadorAtual = "O" if jogadorAtual == "X" else "X"
                
        else:
            print("Jogada inválida. Tente novamente")
            

jogoDaVelha()
            
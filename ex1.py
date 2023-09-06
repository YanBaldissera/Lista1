def criarTabuleiro():
    """ Vai retornar o tabuleiro """
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    return tabuleiro
    
        
def tabuleiro(tabuleiro):
    "vai imprimir o tabuleiro no formato"
    for linha in tabuleiro:
        print("  |  ".join(linha))
        print("-" * 20)
    

def verificarVitoria(tabuleiro, jogador):
    """ Vai retornar se já houve algum ganhador ou não """
    for linhas in tabuleiro:
        if all(posicao == jogador for posicao in linhas):
            return True
    
    for colunas in range(4):
        colunaAtual = [tabuleiro[linhas][colunas] for linhas in range(4)]
        
        if all(posicao == jogador for posicao in colunaAtual):
            return True
        
    
    diagonalPrimaria = [tabuleiro[i][i] for i in range(4)]
    if all(posicao == jogador for posicao in diagonalPrimaria):
        return True
    
    diagonalSecundaria = [tabuleiro[i][3 - i] for i in range(4)]
    if all(posicao == jogador for posicao in diagonalSecundaria):
        return True
    
    
    return False



def jogoDaVelha():
    """ Vai retornar o jogo """
    
    jogo = criarTabuleiro()
    
    jogadorAtual = "X"
    
    while True:
        tabuleiro(jogo)
        
        print(f"Jogador {jogadorAtual}, é a sua vez.")
        linha = int(input("Digite o número da linha (0-3)"))    
        coluna = int(input("Digite o número da coluna (0-3)"))
        
        if 0 <= linha < 4 and 0 <= coluna < 4 and jogo[linha][coluna] == " ":
            jogo[linha][coluna] = jogadorAtual
            
            if verificarVitoria(jogo, jogadorAtual):
                tabuleiro(jogo)
                print(f"Jogador {jogadorAtual} venceu!!!")
                break
            else:
               jogadorAtual = "O" if jogadorAtual == "X" else "X"
                
        else:
            print("Jogada inválida. Tente novamente")
            

jogoDaVelha()
            
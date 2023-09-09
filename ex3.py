""" Para o jogo do termo utilizei a biblioteca que o professor falou na aula sobre as cores. Utilizei a mesma função de leitura 
arquivo do código da forca. depois temos uma função para selecionar uma palavra aleátoria do arquivo de tamanho 5. A função mostrarAlfabeto
para retorna o alfabeto e vai removendo a cada tentativa as letras que já foram utilizadas. A função verificacaoDaPalavrafunção 
compara a palavra escolhida com a tentativa do jogador e retorna a tentativa colorida com base nas correspondências com a palavra 
escolhida. Depois temos o jogo aonde fazemos as solicitações para os usuários e fazemos as verificações e chamadas das funções"""

import random
from termcolor import colored

arquivo = "lista_palavras.txt"  # altere o caminho se necessário
# o ideal é que esteja no mesmo diretório do programa

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]  # método strip remove o '\n' do final da linha

lista = le_arquivo(arquivo)
alfabeto = "abcdefghijklmnopqrstuvwxyz"
palavras = [palavra for palavra in lista if len(palavra) == 5]

def selecionaPalavra():
    """Vai retornar uma palavra aleatoriamente do arquivo """
    palavraEscolhida = random.choice(palavras)
    return palavraEscolhida

def mostrarAlfabeto(letrasTentadas):
    """Retorna o alfabeto com as letras que já foram utilizadas removidas"""
    alfabeto_completo = list(alfabeto)
    for letra in letrasTentadas:
        if letra in alfabeto_completo:
            alfabeto_completo.remove(letra)
    return "Alfabeto restante: " + " ".join(alfabeto_completo)

def mostrarTentativasAnteriores(tentativas_anteriores):
    """Imprime no jogo as tentativas anteriores"""
    for i, (tentativa, resultado) in enumerate(tentativas_anteriores):
        palavra_mostrada = " ".join(resultado)
        print(f"Tentativa {i + 1}: {palavra_mostrada}")

def verificacaoDaPalavra(palavra, tentativa, palavra_escondida):
    """Retorna a palavra colorida"""
    tentativa_colorida = [''] * len(palavra)

    for i in range(len(palavra)):
        if palavra[i] == tentativa[i]:
            tentativa_colorida[i] = colored(tentativa[i], 'green')
        elif tentativa[i] in palavra:
            tentativa_colorida[i] = colored(tentativa[i], 'yellow')
        else:
            tentativa_colorida[i] = colored(tentativa[i], 'black')

    for i, letra_colorida in enumerate(tentativa_colorida):
        if letra_colorida:
            palavra_escondida[i] = letra_colorida

    return tentativa_colorida

palavraEscolhida = selecionaPalavra()
palavraEscondida = ['*'] * len(palavraEscolhida)

vida = 6
tentativas = 0
letras_tentadas = []
tentativasAnteriores = []

print("\nBem-vindo ao jogo Termo!\n")

while vida != 0:
    mostrarTentativasAnteriores(tentativasAnteriores)
    print(mostrarAlfabeto(letras_tentadas))
    tentativa = input("Entre com a palavra desejada com um tamanho de 5 letras: ").lower()

    if tentativa == palavraEscolhida:
        palavraEscondida = list(palavraEscolhida)
        print(f"Você acertou! A palavra era: {palavraEscolhida}")
        break

    letras_tentadas.extend(tentativa)

    tentativaColorida = verificacaoDaPalavra(palavraEscolhida, tentativa, palavraEscondida)
    vida -= 1
    tentativas += 1

    tentativasAnteriores.append((tentativa, tentativaColorida.copy()))

    if tentativas < 6:
        print(f"Tentativas restantes: {6 - tentativas}")

    if vida == 0:
        print(f"Você perdeu. A palavra era: {palavraEscolhida}")
    elif tentativas == 6:
        print("Você usou todas as tentativas. A palavra era:", palavraEscolhida)

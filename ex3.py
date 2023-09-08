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
palavras = [palavra for palavra in lista if len(palavra) == 5]  # Filtro para palavras de tamanho 5

def selecionaPalavra():
    """Vai retornar uma palavra aleátoriamente do arquivo """
    palavraEscolhida = random.choice(palavras)
    return palavraEscolhida

def palavraOculta(palavra):
    return ['*'] * len(palavra)

def mostrarAlfabeto(letrasTentadas):
    alfabeto_completo = list(alfabeto)
    for letra in letrasTentadas:
        if letra in alfabeto_completo:
            alfabeto_completo.remove(letra)
    return "Alfabeto restante: " + " ".join(alfabeto_completo)

def mostrarTentativasAnteriores(tentativas_anteriores):
    for i, (tentativa, cores) in enumerate(tentativas_anteriores):
        print(f"Tentativa {i + 1}: ", end="")
        for letra, cor in cores:
            print(colored(letra, cor), end=" ")
        print()

def verificacaoDaPalavra(palavra, tentativa):
    correto = []
    incorretas = []
    posicoes_incorretas = []

    for i in range(len(palavra)):
        if palavra[i] == tentativa[i]:
            correto.append((palavra[i], 'green'))
        elif tentativa[i] in palavra:
            incorretas.append((tentativa[i], 'yellow'))
            posicoes_incorretas.append(i)
        else:
            incorretas.append((tentativa[i], 'red'))

    return correto, incorretas, posicoes_incorretas

palavraEscolhida = selecionaPalavra()
palavraEscondida = palavraOculta(palavraEscolhida)

acerto = len(palavraEscolhida)
vida = 6
tentativas = 0
letras_tentadas = []
tentativas_anteriores = []

print("\nBem-vindo ao jogo Termo!\n")

while vida != 0:
    print("Palavra escondida:", " ".join(palavraEscondida))
    mostrarTentativasAnteriores(tentativas_anteriores)
    print(mostrarAlfabeto(letras_tentadas))
    tentativa = input("Entre com a palavra desejada: ").lower()

    if tentativa == palavraEscolhida:
        palavraEscondida = list(palavraEscolhida)
        print(f"Você acertou! A palavra era: {palavraEscolhida}")
        break

    letras_tentadas.extend(tentativa)  # Adiciona as letras tentadas à lista

    corretas, incorretas, posicoes_incorretas = verificacaoDaPalavra(palavraEscolhida, tentativa)
    vida -= 1
    tentativas += 1

    tentativas_anteriores.append((tentativa, corretas + incorretas))  # Adiciona a tentativa atual e suas cores às tentativas anteriores

    if tentativas < 6:
        print("Letras corretas:", end=" ")
        for letra, cor in corretas:
            print(colored(letra, cor), end=" ")
        print()  # Adicione esta linha para imprimir uma nova linha no final

        print("Letras incorretas:", end=" ")
        for letra, cor in incorretas:
            print(colored(letra, cor), end=" ")
        print()  # Adicione esta linha para imprimir uma nova linha no final

        print(f"Tentativas restantes: {6 - tentativas}")

    if vida == 0:
        print(f"Você perdeu. A palavra era: {palavraEscolhida}")
    elif tentativas == 6:
        print("Você usou todas as tentativas. A palavra era:", palavraEscolhida)
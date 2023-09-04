def tabuleiro():
    cont = 0
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    for linha in tabuleiro:
        print(f"{cont}".join(linha))
        print(f"{cont}")
        print("  |  ".join(linha))
        print("-" * 20)
        cont += 1
        

tabuleiro()
    
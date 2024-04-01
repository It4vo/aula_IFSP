def verifica_campeao(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != " ":
            return True;

def mostra_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("----------")

tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]



for linha in tabuleiro:
    print(" | ".join(linha))
    print("----------")

rodada = 0

while rodada < 9:
    linha = int(input("Digite uma linha (0, 1, 2):"))
    coluna = int(input("Digite uma coluna (0, 1, 2):"))

    if tabuleiro[linha][coluna] == " ":
        if (rodada%2 == 0):
            tabuleiro[linha][coluna] = "X"
        else:
            tabuleiro[linha][coluna] = "O"

        if verifica_campeao (tabuleiro):
            mostra_tabuleiro(tabuleiro)
            print("Vitória!")
            break
            
        mostra_tabuleiro(tabuleiro)

        rodada += 1
    else:
        print("Casa já ocupada!")

    if rodada == 9:
        mostra_tabuleiro(tabuleiro)
        print("Velha!")


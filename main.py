from tictactoe import *
from minimax import *
from random_player import *
print("Bem vindo ao jogo da velha!\n")
opcoes = ["X", "O"]
tipo = input("Escolha se você (ou o random_player) será X ou O: ")
player = opcoes.pop(opcoes.index(tipo))
vez = "X"
random = True
empate = 0
x = 0
o = 0 
printcerquilha(cerquilha)
for i in range(100):
    while not terminal(cerquilha):
        if vez == player:
            if random:
                posicao = random_choice(cerquilha)
                cerquilha[posicao[0]][posicao[1]] = player
            else:
                print("\nPosições possíveis\n")
                acoes = [posica_num(i) for i in actions(cerquilha)]
                print(acoes)
                posicao = int(input("\nDigite a posição que deseja jogar: "))
                if posicao in acoes:
                    linha, coluna = num_posica(posicao)
                    cerquilha[linha][coluna] = player
                else:
                    print("Posição inválida, tente novamente")
            vez = opcoes[0]
            printcerquilha(cerquilha)
        else:
            posic = minimax(cerquilha, vez)
            cerquilha[posic[0]][posic[1]] = vez
            vez = player
            printcerquilha(cerquilha)

    resultado = terminal(cerquilha)
    if resultado == "Empate":
        print("\nEmpate!")
        empate += 1
    elif resultado == 'X':
        print("\nO vencedor é X!")
        x += 1
    elif resultado == 'O':
        print("\nO vencedor é O!")
        o += 1
            
    reset_cerquilha(cerquilha)
    vez = "X"

print(f"\nResultados após 100 partidas:")
print(f"Vitórias do X: {x}")
print(f"Vitórias do O: {o}")
print(f"Empates: {empate}")
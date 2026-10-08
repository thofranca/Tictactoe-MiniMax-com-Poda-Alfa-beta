from tictactoe import *
from minimax import *
from random_player import *
from alphabet import *
import random

random.seed(1985)
random = False
usa_alfabeta = False
cem_mov = False

print("Bem vindo ao jogo da velha!\n")
print("Regras:\n- O objetivo do jogo é conseguir três símbolos em linha reta\n- As linhas podem ser na horizontal, vertical ou diagonal\n- O jogador que conseguir três símbolos em linha reta vence\n- Se todas as posições forem preenchidas e ninguém conseguir três símbolos em linha reta, o jogo termina em empate")
print("\nComo jogar:\n- Será disponibilizado uma lista de posições vazias, digite o número da posição correspondente.\n")
print("\nConfigurações:\nEscolha o modo de jogo/demonstração.")

while True:
    print("1 - Jogar contra o agente minimax")
    print("2 - Jogar contra o agente minimax alphabet")
    print("3 - Random_player contra o agente minimax")
    print("4 - Random_player contra o agente minimax alphabet")
    jogo = input("\nDigite um número dentro das opções: ")
    if jogo in ["3", "4"]:
        while True:
            resp = input("Executar 100 jogos? (s/n): ")
            if resp.lower() == "s":
                cem_mov = True
                break
            elif resp.lower() == "n":
                cem_mov = False
                break
            else:
                print("Resposta inválida, tente novamente")
    if jogo == "1":
        break
    elif jogo == "2":
        usa_alfabeta = True
        break
    elif jogo == "3":
        random = True
        break
    elif jogo == "4":
        random = True
        usa_alfabeta = True
        break
    else:
        print("Opção inválida, tente novamente")

opcoes = ["X", "O"]
tipo = None
while tipo not in ["X", "O"]:
    tipo = input("Escolha se você (ou o random_player) será X ou O: ")
    tipo = tipo.upper()
    if tipo not in opcoes:
        print("Opção inválida, tente novamente")
player = opcoes.pop(opcoes.index(tipo))
vez = "X"
empate = 0
x = 0
o = 0 
estados_expandidos = [0]
if cem_mov:
    num_jogos = 100
else:
    num_jogos = 1
printcerquilha(cerquilha)
for i in range(num_jogos):
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
                while posicao not in acoes:
                    print("Posição inválida, tente novamente")
                    posicao = int(input("\nDigite a posição que deseja jogar: "))
                linha, coluna = num_posica(posicao)
                cerquilha[linha][coluna] = player
            vez = opcoes[0]
            printcerquilha(cerquilha)
        else:
            if usa_alfabeta:
                posic, valor = alphabeta(cerquilha, vez, estados_expandidos)
            else:
                posic, valor = minimax(cerquilha, vez, estados_expandidos)
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

if cem_mov:
    print(f"\nResultados após 100 partidas:")
    print(f"Vitórias do X: {x}")
    print(f"Vitórias do O: {o}")
    print(f"Empates: {empate}")
    
    algo_name = "Alfa-beta" if usa_alfabeta else "Minimax"
    max_str = "Aleatório" if player == "X" else algo_name
    min_str = "Aleatório" if player == "O" else algo_name
    
    print("\n" + "-"*80)
    print(f"{'MAX':<15} | {'MIN':<15} | {'Vitórias MAX':<15} | {'Empates':<10} | {'Vitórias MIN':<15}")
    print("-" * 80)
    print(f"{max_str:<15} | {min_str:<15} | {x:<15} | {empate:<10} | {o:<15}")
    print("-" * 80 + "\n")
print(f"Estados expandidos pelo agente: {estados_expandidos[0]}")
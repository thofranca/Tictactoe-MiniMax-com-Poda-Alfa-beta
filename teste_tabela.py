from tictactoe import cerquilha, printcerquilha
from minimax import minimax
from alphabet import alphabeta

def whose_turn(state):
    x_count = sum(row.count('X') for row in state)
    o_count = sum(row.count('O') for row in state)
    if x_count > o_count:
        return 'O'
    else:
        return 'X'

estado_1 = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

estado_2 = [
    ["X", " ", " "],
    [" ", "O", " "],
    ["X", " ", " "]
]


estado_3 = [
    ["X", "O", "X"],
    ["O", "X", " "],
    [" ", " ", " "]
]

estados = [estado_1, estado_2, estado_3]

print(f"{'Estado':<8} | {'Algoritmo':<12} | {'Valor':<6} | {'Jogada Escolhida':<18} | {'Estados Expandidos'}")
print("-" * 75)

for i, estado in enumerate(estados):
    player = whose_turn(estado)
    
    cont_minimax = [0]
    acao_min, valor_min = minimax(estado, player, cont_minimax)

    cont_alfa = [0]
    acao_alfa, valor_alfa = alphabeta(estado, player, cont_alfa)
    
    print(f"{i+1:<8} | {'Minimax':<12} | {valor_min:<6} | {str(acao_min):<18} | {cont_minimax[0]}")
    print(f"{i+1:<8} | {'Alfa-beta':<12} | {valor_alfa:<6} | {str(acao_alfa):<18} | {cont_alfa[0]}")
    print("-" * 75)

# Jogo da Velha com Minimax e Poda Alfa-Beta

O objetivo principal do projeto é a implementação de um agente capaz de jogar o **Jogo da Velha** de forma ótima utilizando o algoritmo **Minimax**, bem como otimizar essa busca utilizando a **Poda Alfa-Beta**.

## Como Executar

Certifique-se de que possui o Python 3 instalado na sua máquina.

### Jogo Principal (`main.py`)
Para jogar contra o agente ou para colocar o Agente Aleatório para batalhar contra o Minimax/Alfa-Beta, execute:

```bash
python main.py
```

Você terá acesso a um menu inicial onde pode escolher:
1. Jogar contra o agente Minimax.
2. Jogar contra o agente Minimax com Alfa-Beta.
3. Colocar o Agente Aleatório para jogar contra o Minimax.
4. Colocar o Agente Aleatório para jogar contra o Alfa-Beta.

**Nota:** Ao escolher as opções `3` ou `4`, você terá a opção de automatizar **100 partidas consecutivas**, e no fim da execução será exibida uma tabela de estatísticas comparando a performance e o número de estados da árvore que foram expandidos pelo agente.

### Gerador de Tabela Comparativa (`teste_tabela.py`)
Para fins de relatório, foi criado um script focado exclusivamente em demonstrar a diferença de expansão de estados entre os algoritmos para 3 cenários específicos (Tabuleiro vazio e mais 2 estados customizados). Para visualizar a tabela de eficiência, rode:

```bash
python teste_tabela.py
```

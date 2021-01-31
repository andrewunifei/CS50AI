# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 29/01/2021
#
# Os conteúdos de todas as funções, exceto a initial_state, foram implementados por mim

"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    # Retorna o estado inicial do board
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Retorna o jogador da próxima rodada
    count = 0

    for row in board:
        for status in row:
            if status != EMPTY:
                count += 1
                
    if count % 2 == 0:
        return X
    else:
        return O

def actions(board):
    # Retorna um set de todas as ações (i, j) possíveis disponíveis no board
    possible_actions = set()

    for i, row in enumerate(board):
        for j, status in enumerate(row):
            if status == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    # Retorna o board que resulta do movimento (i, j)
    current_player = player(board)
    board[action[0]][action[1]] = current_player

    return board


def winner(board):
    # Retorna o vencedor do jogo, se existe algum
    retrieve = []

    possibilities = (
        ((0, 0), (0, 1), (0, 2)), # Linhas horizontais
        ((1, 0), (1, 1), (1, 2)), 
        ((2, 0), (2, 1), (2, 2)), 

        ((0, 0), (1, 0), (2, 0)), # Linhas verticais
        ((0, 1), (1, 1), (2, 1)), 
        ((0, 2), (1, 2), (2, 2)), 

        ((0, 0), (1, 1), (2, 2)), # Linhas diagonais
        ((0, 2), (1, 1), (2, 0))  
    )

    for row in possibilities:
        countX = 0
        countO = 0
        
        for pair in row:
            if board[pair[0]][pair[1]] == X:
                countX += 1
            elif board[pair[0]][pair[1]] == O:
                countO += 1 

            if countX == 3:
                return X
            elif countO == 3:
                return O

    return None

def terminal(board):
    # Retorna True se o jogo acabou. Senão, retorna False
    if winner(board) != None:
        return True

    for row in board:
        for status in row:
            if status == EMPTY:
                return False
    
    return True


def utility(board):
    # Retorna 1 se o X ganhou o jogo, -1 se o O ganhou ou 0 se empate
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def min_value(board):
    if terminal(board):
        return utility(board), ()
    v = 9999

    for action in actions(board):
        value, aktion = max_value(result(board, action))
        v = min(v, value)

    return v, action

def max_value(board):
    if terminal(board):
        return utility(board), ()
    v = -9999

    for action in actions(board):
        value, aktion = min_value(result(board, action))
        v = max(v, value)

    return v, action

def minimax(board):
    # Retorna a ação ótima do jogador atual

    boardClone = copy.deepcopy(board)
    current_player = player(board)

    if current_player == O:
        if(not terminal(boardClone)):
            v, action = min_value(boardClone)

            return action # Mudar isso
        else:
            return None
    else:
        if(not terminal(boardClone)):
            v, action = max_value(boardClone)

            return action # Mudar isso
        else:
            return None

def winner(board):
    # Retorna o vencedor do jogo, se existe algum

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
            if board[pair[0]][pair[1]] == 'X':
                countX += 1
            elif board[pair[0]][pair[1]] == 'O':
                countO += 1 

            if countX == 3:
                return 'X'
            elif countO == 3:
                return 'O'

    return None

l = [
        ['X', 'O', 'O'],
        ['O', 'X', 'X'],
        ['X', 'O', 'X']
    ]

print(winner(l))
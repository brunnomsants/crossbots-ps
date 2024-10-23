def isValidSudoku(board):
    row = [[] for _ in range(9)]
    column = [[] for _ in range(9)]
    group = [[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            n = board[i][j]
            if n!='.':
                index = (i // 3) * 3 + (j // 3)
                if n in column[j] or n in row[i] or n in group[index]:
                    return False
                
                row[i].append(n)
                column[j].append(n)
                group[index].append(n)
                
    return True
    

def board():
    board = [[] for i in range(9)]
    for i in range(0, 9):
        board[i] = input().split()
    return print(isValidSudoku(board))

board() 




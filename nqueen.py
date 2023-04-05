def isSafe(board, row, col):
    # to check if the queen is avaliable in the same column or not
    
    
    #  \  |  /
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    (i, j) = (row, col)
    # to check the left diagonal
    while i >= 0 and j >= 0:    
        if board[i][j] == 'Q':
            return False
        j = j-1
        i = i-1
    # to check the  right diagonal
    (i, j) = (row, col)
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i = i-1
        j = j+1

    return True

# to print the solution


def printsolution(board):
    for r in board:
        print(str(r).replace(',', '').replace('\'', ''))
    print()

# to solve the n queen problem


def nqueen(board, row):
    if row == len(board):
        printsolution(board)
        return

    for i in range(len(board)):
        if isSafe(board, row, i):
            # to check if the block is safe or not if the block is safe then place the queeen
            board[row][i] = 'Q'
            # if the block is safe and queen is placed then move to next row
            nqueen(board, row+1)
            # while backtracking remove the queen and then bakctrack
            board[row][i] = '-'


if __name__ == '__main__':
    N = 4
    mat = [['–' for x in range(N)] for y in range(N)]
    #calling the function
    nqueen(mat, 0)
    
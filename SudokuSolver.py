#This function makes sure that the move is valid
#also checks for repeated numbers in the same line

def valid_move(board, row, col, number):
    #checks if the number repeats in the column or row
    for x in range(9):
        if board[row][x] == number:
            return False

    for x in range(9):
        if board[x][col] == number:
            return False

    #recognizes the corner row
    cornerRow = row - row % 3
    cornerCol = col - col % 3

    for x in range(3):
        for y in range(3):
            if board[cornerRow + x][cornerCol + y] == number:
                return False
            
    return True

#uses recursion to add numbers
def solution(board, row, col):

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if board[row][col] > 0:
        return solution(board, row, col + 1)

    for num in range(1,10):
        # if valid, set the value of the space to the number
        if valid_move(board, row, col, num):

            board[row][col] = num

            if solution(board, row, col + 1):
                return True

        board[row][col] = 0

    return False

#example board    
board =  [[4,0,0,6,0,0,0,7,1],
          [0,0,8,3,0,0,0,2,0],
          [0,9,0,0,0,0,5,0,0],
          [6,0,0,1,0,0,0,3,7],
          [0,0,7,0,0,0,9,0,0],
          [2,0,0,0,4,8,0,0,0],
          [0,0,2,0,7,0,0,0,6],
          [1,0,0,9,5,0,0,0,0],
          [5,0,0,0,6,1,0,0,4]]

if solution(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
        print()
else:
    print("No Solution")
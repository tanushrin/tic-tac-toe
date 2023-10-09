def display_board(board, width):
    tic_str = ""
    '''
    for index, piece in enumerate(board):
        #if index == 0:
            #tic_str += piece
        if index!=0 and index%width == 0:
            tic_str +=  "\n" + piece
        else:
            tic_str +=  piece
    '''
    separator = (width*3)+width-1
    for index in range(len(board)):
        tic_str += f' {board[index]} '
        if index+1 < len(board):
            if (index+1) % width == 0:
                tic_str += '\n' + ('-'*separator) + '\n'
            else:
                tic_str += '|'

    return tic_str


print(display_board(["O", "X", "X", "O"],2))
print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " "],3))
print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"],5))

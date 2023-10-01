class ColumnOverflow(Exception):
    pass


def free_slot(col, slots):
    row = len(slots)-1  # Getting the bottom row's index
    while row >= 0:
        slot = slots[row][col]
        if slot == 0:   # Checking if the bottom of the column is free
            return col, row
        else:
            row -= 1
    raise ColumnOverflow("No free slots in the column")  # If no free spaces in the column throw exception


def submatrices_4x4(matrix):    # Returns a list of all the unique by indices 4x4 submatrices
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    submatrices = []
    for rows in range(matrix_rows-3):
        for cols in range(matrix_columns-3):    # Going through the topleft coordinates of all the 4x4 matrices
            submatrix = []
            for i in range(4):
                row = []
                i += rows
                for j in range(4):
                    j += cols
                    row.append(matrix[i][j])
                submatrix.append(row)   # Getting the 4x4 matrix by its topleft coordinate
            submatrices.append(submatrix)
    return submatrices


def check_winner(matrix):
    submatrices = submatrices_4x4(matrix)
    for submatrix in submatrices:
        for row in submatrix:   # Checking the rows for winner
            unique_row = list(set(row))    # We turn every set into list to be able to access the item in it
            if len(unique_row) == 1 and unique_row[0] != 0:
                return unique_row[0]

        for col_index in range(4):  # Checking all the columns for winner
            column = []
            for row_index in range(4):
                column.append(submatrix[row_index][col_index])
            unique_column = list(set(column))
            if len(unique_column) == 1 and unique_column[0] != 0:
                return unique_column[0]
        main_diag = []
        sec_diag = []
        for i in range(4):  # Getting the diagonals
            main_diag.append(submatrix[i][i])
            sec_diag.append(submatrix[-(i+1)][i])   # We take -(i+1) coz it starts with 0;0 instead of -1;0

        unique_main_diag = list(set(main_diag))
        unique_sec_diag = list(set(sec_diag))
        if len(unique_main_diag) == 1 and unique_main_diag[0] != 0:
            return unique_main_diag[0]
        if len(unique_sec_diag) == 1 and unique_sec_diag[0] != 0:
            return unique_sec_diag[0]


board = []
# ____________________________
board_rows = int(input("Rows[1-39]>>"))         # Custom board with size validation
while not (0 < board_rows < 40):
    board_rows = int(input("Rows[1-39]>>"))

board_columns = int(input("Columns[1-39]>>"))
while not (0 < board_columns < 40):
    print()
    board_columns = int(input("Columns[1-39]>>"))
    # ____________________________
for _ in range(board_rows):  # Generating the board
    row = []
    for _ in range(board_columns):
        row.append(0)
    board.append(row)
    # ____________________________
players = int(input("Number of players>>"))
winner = None
while True:
    for player_num in range(1, players+1):
        while True:
            player = int(input(f"Player {player_num}, please choose a column [1-{board_columns}]>>")) - 1
            try:
                slot = free_slot(player, board)
                break
            except IndexError:
                print("Please enter a valid number!")
        board[slot[1]][slot[0]] = player_num
        winner = check_winner(board)
        if winner is not None:
            break
    for row in board:
        print(row)
    if winner is not None:
        break

print(f"The winner is player {winner}")
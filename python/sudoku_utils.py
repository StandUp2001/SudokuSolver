def is_valid(sudoku: list[list[int]], row: int, col: int) -> bool:
    return not cell_in_row_or_col(sudoku, row, col) and not cell_in_square(sudoku, row, col)


def cell_in_row_or_col(sudoku: list[list[int]], row: int, col: int) -> bool:
    for i in range(9):
        if (i != row and sudoku[i][col] == sudoku[row][col]) or (i != col and sudoku[row][i] == sudoku[row][col]):
            return True
    return False


def cell_in_square(sudoku: list[list[int]], row: int, col: int) -> bool:
    for i in range(3):
        for j in range(3):
            if (i != row % 3 or j != col % 3) and sudoku[row - row % 3 + i][col - col % 3 + j] == sudoku[row][col]:
                return True
    return False

from driver_utils import (
    create_driver,
    create_row,
    get_rows,
    get_star_number,
    get_game_id,
    print_sudoku,
)
from sudoku_utils import is_valid


def get_sudoku() -> list[list[int]] | None:
    url = "https://www.sudokuonline.nl"
    star_number = get_star_number()
    print(f"Getting and solving sudoku from '{url}' with {star_number} stars.")
    driver = create_driver()
    game_id = get_game_id(driver, star_number)
    if game_id is None:
        print(f"Could not find a sudoku with {star_number} stars.")
        return None
    sudoku = [create_row(row) for row in get_rows(driver, game_id)]
    driver.close()
    return sudoku


def solve(sudoku: list[list[int]]) -> bool:
    # sudoku solver recursive
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] != 0:
                continue
            for number in range(1, 10):
                sudoku[row][col] = number
                if is_valid(sudoku, row, col) and solve(sudoku):
                    return True
                sudoku[row][col] = 0
            return False
    return True


def main() -> None:
    # Get the sudoku
    sudoku = get_sudoku()
    if sudoku is None:
        print("Could not get the sudoku.")
        return

    # Print the sudoku without solution
    print_sudoku(sudoku)

    # Solve the sudoku
    if not solve(sudoku):
        print("Could not solve the sudoku.")
        return

    # Print the solution
    print_sudoku(sudoku)


if __name__ == "__main__":
    main()

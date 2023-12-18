import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement


def create_driver() -> webdriver.Firefox:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.sudokuonline.nl')
    return driver


def get_game_id(driver: webdriver.Firefox, star_number: int) -> str | None:
    for sudoku_difficulty in driver.find_elements(By.CLASS_NAME, "sudoku_difficulty"):
        if len(sudoku_difficulty.find_elements(By.TAG_NAME, "img")) == star_number:
            return get_id_from_element(sudoku_difficulty)
    return None


def print_sudoku(sudoku: list[list[int]]) -> None:
    line = '-'*25
    print(line)
    for i in range(9):
        print('|', end='')
        for j in range(9):
            text = '  '
            if sudoku[i][j] != 0:
                text = f' {sudoku[i][j]}'
            print(text, end='')
            if j % 3 == 2:
                print(' |', end='')
        print()
        if i % 3 == 2:
            print(line)


def get_star_number() -> int:
    default = 4
    if len(sys.argv) > 1:
        try:
            default = int(sys.argv[1])
        except ValueError:
            print(f'Invalid star number. Using default value {default}.')
    if not 1 <= default <= 5:
        print(f'Invalid star number. Using default value {default}.')
        default = 4
    return default


def get_id_from_element(element: WebElement) -> str:
    el = element.get_attribute("id")
    if el is not None:
        return el.replace('player', '').replace("_difficulty", "")
    return ""


def get_rows(driver: webdriver.Firefox, game_id: str) -> list[WebElement]:
    return driver.find_element(By.ID, f"player{game_id}_game").find_elements(By.TAG_NAME, "tr")


def create_row(row: WebElement) -> list[int]:
    return [get_number(cell) for cell in row.find_elements(By.TAG_NAME, "td")]


def get_number(cell: WebElement) -> int:
    attributes = cell.get_attribute("innerHTML")
    if attributes is None:
        return 0
    if len(attributes) == 1:
        return int(attributes)
    return 0

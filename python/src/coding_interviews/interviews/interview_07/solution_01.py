def valid_queen_pos(columns: list[int], row: int, col: int) -> bool:
    for existing_row, existing_col in enumerate(columns):
        if col == existing_col:
            return False
        elif abs(row - existing_row) == abs(col - existing_col):
            return False

    return True


def place_queens(n: int) -> list[list[int]]:
    results: list[list[int]] = []

    def queen_r(columns: list[int]):
        row = len(columns)
        if row == n:
            results.append(columns)
        for col in range(0, n):
            if valid_queen_pos(columns, row, col):
                queen_r(columns + [col])

    queen_r([])
    return results

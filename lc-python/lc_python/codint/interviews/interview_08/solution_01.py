from copy import deepcopy


def compute_pond_size(land: list[list[int]], r: int, c: int) -> int:
    if r < 0 or r >= len(land) or c < 0 or c >= len(land[r]) or land[r][c] != 0:
        return 0

    size: int = 1
    land[r][c] = -1

    for dr in range(-1, 1 + 1):
        for dc in range(-1, 1 + 1):
            size += compute_pond_size(land, r + dr, c + dc)

    return size


def compute_pond_sizes(land: list[list[int]]) -> list[int]:
    sizes: list[int] = []
    editable_land = deepcopy(land)

    for r in range(len(editable_land)):
        for c in range(len(editable_land[r])):
            if editable_land[r][c] == 0:
                sizes.append(compute_pond_size(editable_land, r, c))

    return sizes

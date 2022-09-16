def one_edit_away(first: str, second: str) -> bool:
    lenght_first = len(first)
    lenght_second = len(second)

    if abs(lenght_first - lenght_second) > 1:
        return False

    diffs = 0
    idx_first = 0
    idx_second = 0

    while idx_first < lenght_first and idx_second < lenght_second:
        if first[idx_first] == second[idx_second]:
            idx_first += 1
            idx_second += 1
        else:
            diffs += 1
            if diffs > 1:
                return False

            if lenght_first > lenght_second:
                idx_first += 1
            elif lenght_second > lenght_first:
                idx_second += 1
            else:
                idx_first += 1
                idx_second += 1

    return True

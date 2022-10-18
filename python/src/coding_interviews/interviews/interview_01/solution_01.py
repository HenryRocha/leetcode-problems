def one_replacement_away(first: str, second: str) -> bool:
    diffs = 0
    for fc, sc in zip(first, second):
        if fc != sc:
            diffs += 1

        if diffs >= 2:
            return False

    return True


def one_insertion_away(shorter: str, longer: str) -> bool:
    si = 0
    li = 0
    while si < len(shorter) and li < len(longer):
        if shorter[si] == longer[li]:
            si += 1
            li += 1
        else:
            li += 1

    if li - si > 1:
        return False

    return True


def one_edit_away(first: str, second: str) -> bool:
    length_diff = len(first) - len(second)
    if length_diff == 0:
        return one_replacement_away(first, second)
    elif length_diff == 1:
        # First is longer than second.
        return one_insertion_away(second, first)
    elif length_diff == -1:
        # Second is longer than first.
        return one_insertion_away(first, second)

    return False

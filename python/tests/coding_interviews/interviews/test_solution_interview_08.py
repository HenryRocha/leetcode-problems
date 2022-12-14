from typing import Callable

import pytest
from _pytest.fixtures import SubRequest
from src.coding_interviews.interviews.interview_08.solution_01 import compute_pond_sizes as compute_pond_sizes_s1

ComputePondSizesFuncType = Callable[[list[list[int]]], list[int]]


@pytest.fixture(params=[compute_pond_sizes_s1])
def implementation(request: SubRequest) -> ComputePondSizesFuncType:
    return request.param


@pytest.mark.parametrize(
    "land, expected",
    [
        (
            [
                [0],
            ],
            [1],
        ),
        (
            [
                [1],
            ],
            [],
        ),
        (
            [
                [0, 2, 1, 0],
                [0, 1, 0, 1],
                [1, 1, 0, 1],
                [0, 1, 0, 1],
            ],
            [1, 2, 4],
        ),
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            [16, 16],
        ),
        (
            [
                [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
            ],
            [10, 19, 19],
        ),
    ],
)
def test_compute_pond_sizes(implementation: ComputePondSizesFuncType, land: list[list[int]], expected: list[int]):
    orig_land = [[l for l in row] for row in land]
    result = implementation(land)
    land_str = "[\n" + ",\n".join(repr(r) for r in orig_land) + "\n]"

    msg = f"Wrong solution for field \n{land_str} \n. Expected: {expected}. Got: {result}."
    assert len(expected) == len(result), msg
    for e in expected:
        assert e in result, msg
    assert (
        orig_land == land
    ), "The input matrix should remain unchanged (you may modify it during the execution of the function, but must undo the changes before returning)."

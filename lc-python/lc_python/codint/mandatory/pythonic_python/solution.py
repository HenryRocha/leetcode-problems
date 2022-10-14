import math
from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")
ListAnyType = list[Any]


def print_indices_and_elements(elements: ListAnyType) -> None:
    for i, element in enumerate(elements):
        print(i, element)


def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [num for num in range(start, end + 1) if num % 2 == 0]


def get_char_set_from(s: str) -> set[str]:
    return {c for c in s}


def get_perfect_squares_between(start: int, end: int) -> dict[int, int]:
    return {i * i: i for i in range(int(math.sqrt(start)), int(math.sqrt(end)) + 1) if start <= i * i <= end}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [i for i in numbers if i % 2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [n if n % 2 == 0 else -1 for n in numbers if n % 5 == 0]


def str_lengths(strings: list[str]) -> list[int]:
    return [len(s) for s in strings]


def get_fibonacci_type(version: int) -> str:
    return "<class 'generator'>" if version == 1 else "<class 'list'>"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return (
        "Um generator é mais eficiente em questões de memória, já que "
        + "vai gerando novos resultados de acordo a demanda. Já uma "
        + "função que retorna uma lista com a resposta completa não é "
        + "tão eficiente, já que ocupa todo o espaço em memória de uma vez só."
    )


class SkipIterator(Generic[T]):
    def __init__(self, elements: list[T]):
        self.elements = elements
        self.length = len(elements)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self) -> T:
        if self.idx >= self.length:
            raise StopIteration

        self.idx += 2
        return self.elements[self.idx - 2]


def my_avg(e1: float, e2: float, *others: float) -> float:
    total = e1 + e2
    for other in others:
        total += other
    return total / (2 + len(others))


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    c = {**a, **b}
    d = {**b, **a}

    return sorted([n for n in c if c[n] != d[n]])


def print_out_in(*numbers: Any) -> None:
    while len(numbers) > 1:
        n1, n2 = numbers[0], numbers[-1]
        print(n1, n2)
        numbers = numbers[1:-1]

    if numbers:
        print(numbers[0])


def append_range(start: int, end: int, step: int = 1, to: Optional[list[int]] = None):
    if to is None:
        to = []

    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10


def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var

    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value: Any):
    return value is None

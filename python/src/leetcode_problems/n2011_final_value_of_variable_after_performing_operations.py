class Solution:
    operations: dict[str, int] = {
        "X++": 1,
        "++X": 1,
        "X--": -1,
        "--X": -1,
    }

    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x: int = 0

        for op in operations:
            x += self.operations[op]

        return x

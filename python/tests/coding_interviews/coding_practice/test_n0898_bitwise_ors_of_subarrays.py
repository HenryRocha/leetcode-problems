from src.coding_interviews.coding_practice.n0898_bitwise_ors_of_subarrays import Solution


def _check(l: list[int], expected: int):
    ret = Solution().subarrayBitwiseORs(l)
    assert ret == expected, f"Wrong answer for input {repr(l)}. Exoected: {expected}. Returned: {ret}"


def test_1():
    _check([], 0)


def test_2():
    _check([1], 1)


def test_3():
    _check([1, 6], 3)


def test_4():
    _check([124, 1, 6], 6)


def test_5():
    _check([255, 124, 1, 6], 7)


def test_6():
    _check([1, 2, 4, 8, 16, 32, 64], 28)


def test_7():
    _check([1, 2, 4, 8, 16, 32, 64, 32, 64, 128, 256, 512, 1024, 2048, 4096], 91)


def test_8():
    _check([1, 2, 4, 8, 1023, 16, 32, 64, 255, 32, 64, 128, 256, 512, 1024, 2048, 4096], 55)


def test_9():
    _check(
        [1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 63, 64, 127, 128, 255, 256, 511, 512, 1023, 1024, 2047, 2048, 4095, 4096], 25
    )


def test_10():
    _check(
        [
            4095,
            2,
            4095,
            4,
            4095,
            8,
            4095,
            16,
            4095,
            32,
            4095,
            64,
            4095,
            128,
            4095,
            256,
            4095,
            512,
            4095,
            1024,
            4095,
            2048,
            4095,
            4096,
        ],
        14,
    )


def test_11():
    _check([250, 250, 250, 250, 250], 1)


def test_12():
    _check([250, 250, 111, 250, 250], 3)

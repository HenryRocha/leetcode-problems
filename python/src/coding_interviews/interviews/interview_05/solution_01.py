def swap_odd_even_bits(x: int) -> int:
    MASK_EVEN = 0b01010101010101010101010101010101
    MASK_ODD = 0b10101010101010101010101010101010

    return ((x & MASK_EVEN) << 1) | ((x & MASK_ODD) >> 1)

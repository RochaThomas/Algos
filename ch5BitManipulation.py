# cracking the coding interview 
# chapter 5 bit manipulation

# interview questions

# 5.1 insertion
# given 2 32-bit numbers, m and n, and two bit positions, i and j. write a function that inserts n into m
# such that m starts at j and ends at i
def insertion(m, n, i, j):
    """
    clear bits from i to j
    shift n to the left to line up with i and j
    return m | n
    """
    frontMask = (-1 << (j + 1))
    backMask = (1 << i)
    mask = frontMask | backMask
    m = m | mask
    n = n << (j + 1)

    return m | n

# 5.2 binary to string
# 
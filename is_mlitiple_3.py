def is_multiple_3(n):
    odd_count = 0
    even_count = 0
    if n < 0:
        n = -n
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n & 1:
        odd_count += 1
    if n & 2:
        even_count += 1
    n = n >> 2

    return is_multiple_3(abs(odd_count-even_count))


num = 997
is_multiple_3(num)

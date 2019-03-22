#!/usr/bin/python
# Benjamin Wiens
# https://www.geeksforgeeks.org/find-the-point-where-a-function-becomes-negative/
# Unbounded Binary Search Example (Find the point where a monotonically increasing function becomes positive first time)


# Monotonocally increasing function
def f(x):
    print("hit", x, x * x - 10 * x - 20)
    return (x * x - 10 * x - 20)

# Binary search implementation
def bin_search(left, right):
    mid = (right + left) // 2
    # found the first positive
    if f(mid) > 0 and f(mid - 1) <= 0:
        return mid
    elif f(mid) <= 0:
        return bin_search(mid + 1, right)
    else:
        return bin_search(left, right - 1)


def find_first_positive(x):
    """Function to return first positive in monotonically increasing fx"""

    # doubling search until we find a positive number
    while f(x) <= 0:
        x *= 2

    result = bin_search(x//2, x)
    return result


print(find_first_positive(25))

# Runtime is Binary Search O(Logn)


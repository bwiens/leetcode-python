#!/usr/bin/python
# Benjamin Wiens
#Fibonacci with and without memoization
import time

def fib_slow(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    elif n > 2:
        return fib_slow(n-1) + fib_slow(n-2)


cache = {}

def fib_dp(n):
    if n in cache:
        return cache[n]
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 1
    elif n > 2:
        value = fib_dp(n-1) + fib_dp(n-2)
        cache[n] = value
        return value

print("starting fib_dp")
start = time.time()
for i in range (0, 33):
    print(i, ": ", fib_dp(i))
end = time.time()
print(end - start)

print("starting fib_slow")
start2 = time.time()
for i in range (0, 33):
    print(i, ": ", fib_slow(i))
end2 = time.time()
print(end2 - start2)

print("---")
print("fib_slow: ", end2-start2)
print("fib_dp: ", end-start)

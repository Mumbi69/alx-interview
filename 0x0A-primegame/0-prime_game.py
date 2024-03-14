#!/usr/bin/python3
"""prime game"""


def count_prime(n):
    """generate a list of prime numbers up to a given n"""
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    count = 0
    for p in range(2, n + 1):
        if prime[p]:
            count += 1
    return count


def isWinner(x, nums):
    """
       determines the winner based on whether the number
       of primes is even or odd
    """
    ben = 0
    maria = 0
    if x <= 0 or not nums:
        return None
    for num in range(x):
        if count_prime(nums[num]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if ben == maria:
        return None
    return "Maria"

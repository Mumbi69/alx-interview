#!/usr/bin/python3
""" Prime Game """


def is_prime(num):
    """check if a number is prime"""
    if (num <= 1):
        return False
    i = 2
    while (i * i) <= num:
        if (num % i) == 0:
            return False
        i += 1
    return True


def primes_up_to_n(n):
    """generate a list of prime numbers up to a given n"""
    primes_up_to_n = 0
    for i in range(2, n + 1):
        if is_prime(i):
            primes_up_to_n += 1
    return primes_up_to_n


def isWinner(x, nums):
    """determines the winner based on whether the number
    of primes is even or odd"""
    ben_w = maria_w = 0

    if x <= 0 or nums is None or len(nums) == 0:
        return None

    for i in range(x):
        if primes_up_to_n(nums[i]) % 2 == 0:
            ben_w += 1
        else:
            maria_w += 1
    if ben_w == maria_w:
        return None
    return 'Ben' if ben_w > maria_w else 'Maria'

#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """check if a number is prime"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to_n(nums):
    """generate a list of prime numbers up to a given n"""
    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
    return count


def isWinner(x, nums):
    """determines the winner based on whether the number
    of primes is even or odd"""
    ben = 0
    maria = 0
    if x <= 0 or not nums:
        return None
    for num in range(x):
        num_arr = [n for n in range(1, nums[num] + 1)]
        if primes_up_to_n(num_arr) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if ben == maria:
        return None
    return "Maria"

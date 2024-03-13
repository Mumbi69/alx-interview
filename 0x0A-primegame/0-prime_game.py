#!/usr/bin/python3
""" Prime Game """


def is_prime(num):
    """check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_up_to_n(n):
    """generate a list of prime numbers up to a given n"""
    return [i for i in range(2, n+1) if is_prime(i)]


def isWinner(x, nums):
    """determines the winner based on whether the number
    of primes is even or odd"""
    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes = get_primes_up_to_n(n)
        num_primes = len(primes)

        if num_primes % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None

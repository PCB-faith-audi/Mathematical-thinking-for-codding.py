def sieve_of_eratosthenes(n):
    """Return a list of all prime numbers up to n (inclusive)."""
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

primes_up_to_50 = sieve_of_eratosthenes(50)
print("Primes up to 50:", primes_up_to_50)
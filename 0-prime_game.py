def isWinner(x, nums):
    """
    Determine the winner of each game and return the player with the most wins.

    :param x: Number of rounds
    :param nums: Array of n values for each round
    :return: Name of the player with the most wins ("Maria", "Ben", or None)
    """
    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n using the Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    def count_primes_up_to(n, prime_flags):
        """Count the number of primes up to n."""
        return sum(prime_flags[:n + 1])

    # Generate the prime sieve for the maximum possible n
    max_n = max(nums)
    prime_flags = sieve_of_eratosthenes(max_n)

    # Count primes for each number up to max_n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if prime_flags[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the number of primes is odd
        else:
            ben_wins += 1  # Ben wins if the number of primes is even

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

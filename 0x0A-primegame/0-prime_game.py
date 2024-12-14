#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Generate a list to check primes and count primes up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    
    # Generate a cumulative count of primes
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)
    
    return prime_count

def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_count = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Number of primes up to n
        primes_up_to_n = prime_count[n]

        # Maria wins if the count of primes is odd
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))



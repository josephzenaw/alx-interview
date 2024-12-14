#!/usr/bin/python3

def is_prime(num):
    """Check if a number is a prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_count(max_n):
    """Generate the cumulative count of primes up to max_n"""
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime(i) else 0)
    return prime_count

def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_count = generate_prime_count(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))


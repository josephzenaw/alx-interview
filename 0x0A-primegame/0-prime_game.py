#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    :param x: Number of rounds (integer).
    :param nums: List of integers, where each integer represents the range of numbers for a round.
    :return: Name of the player that won the most rounds ("Maria" or "Ben"), or None if it's a tie.
    """
    def generate_primes(limit):
        """
        Generate a list indicating prime numbers up to the given limit.
        :param limit: The maximum number to check for primality.
        :return: A list where index i is True if i is prime, False otherwise.
        """
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime

        for i in range(2, limit + 1):
            if primes[i]:
                for j in range(i * 2, limit + 1, i):
                    primes[j] = False
        return primes

    if x < 1 or not nums:
        return None

    max_n = max(nums)  # Find the maximum value in nums
    primes = generate_primes(max_n)  # Precompute prime numbers up to max_n

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of primes up to n
        primes_count = sum(primes[:n + 1])

        # Determine winner for this round
        if primes_count % 2 == 1:  # Maria wins if the count is odd
            maria_wins += 1
        else:  # Ben wins if the count is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))


import numpy as np
import time


def divisors(n):
    """
    This function calculates the proper divisors of a number.
    It returns a list of divisors.
    """
    result = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                result.append(i)
            else:
                result.extend([i, n // i])
    return result


def main():
    """
    This is the main function that calculates the sum of all positive integers
    which cannot be written as the sum of two abundant numbers.
    """
    start_time = time.time()

    # Generate a list of abundant numbers
    abundant_nums = [i for i in range(1, 28124) if sum(divisors(i)) > i]

    # Initialize an array to track the sums of abundant numbers
    abundant_sums = np.full(28124, False)

    # Mark the sums of all pairs of abundant numbers
    for i in abundant_nums:
        for j in abundant_nums:
            if i + j < 28124:
                abundant_sums[i + j] = True
            else:
                break

    # Calculate the sum of numbers that cannot be written as the sum of two abundant numbers
    total = np.sum(np.where(abundant_sums == False)[0])
    end_time = time.time()
    print(f'Answer = {total}')
    print(f"Execution time: {round(end_time - start_time, 2)} seconds")


if __name__ == "__main__":
    main()

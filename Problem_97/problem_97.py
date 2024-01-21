import time


def fast_power(base: int, power: int, mod: int) -> int:
    """
    Calculate fast exponentiation (base^power % mod) using the binary exponentiation algorithm.

    Args:
        base (int): The base of the exponentiation.
        power (int): The exponent.
        mod (int): The modulus.

    Returns:
        int: The result of fast exponentiation.
    """
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        power = power // 2
        base = (base * base) % mod
    return result


if __name__ == "__main__":
    start_time = time.time()

    BASE = 2
    POWER = 7830457
    MOD = 10**10
    
    answer = (28433 * fast_power(BASE, POWER, MOD) + 1) % MOD
    print(f"Answer = {answer}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")

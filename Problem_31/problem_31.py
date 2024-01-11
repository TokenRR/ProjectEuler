import time


def count_combinations(coins, total):
    """
    This function returns the number of combinations to make up a total from given set of coins.

    Parameters:
    coins (list): The list containing the value of available coins.
    total (int): The total amount to be made up from given coins.

    Returns:
    int: The number of combinations to make up the total.
    """
    
    dp = [0] * (total + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] += dp[i - coin]
            
    return dp[total]


if __name__ == "__main__":
    
     # Start the timer
     start_time = time.time()

     # Available UK coins in pence
     uk_coins = [1, 2, 5, 10, 20, 50, 100, 200]

     # Total amount to be made up in pence (£2)
     total_amount = 200

     # Call the function
     combinations = count_combinations(uk_coins, total_amount)

     # Stop the timer
     end_time = time.time()

     print(f'Answer = {combinations}')
     print(f'Elapsed time: {round(end_time - start_time, 2)} seconds')

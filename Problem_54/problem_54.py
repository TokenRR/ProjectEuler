import time
from collections import Counter


CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def evaluate_hand(hand: list) -> tuple:
    """
    Evaluate the given poker hand and return its rank and values.

    Parameters:
    hand (list): A list of strings representing cards in a poker hand.

    Returns:
    tuple: A tuple containing the rank of the hand (int) and its values (list or int).
    """
    sorted_values = sorted((CARD_VALUES[card[0]] for card in hand), reverse=True)
    suits = {card[1] for card in hand}
    value_counts = Counter(sorted_values)

    is_straight = len(value_counts) == 5 and max(sorted_values) - min(sorted_values) == 4
    is_flush = len(suits) == 1

    if is_straight and is_flush:
        return 9, max(sorted_values)  # Royal Flush or Straight Flush
    if value_counts.most_common(1)[0][1] == 4:
        return 8, value_counts.most_common(1)[0][0]  # Four of a Kind
    if value_counts.most_common(2)[0][1] == 3 and value_counts.most_common(2)[1][1] == 2:
        return 7, value_counts.most_common(1)[0][0]  # Full House
    if is_flush:
        return 6, sorted_values  # Flush
    if is_straight:
        return 5, max(sorted_values)  # Straight
    if value_counts.most_common(1)[0][1] == 3:
        return 4, value_counts.most_common(1)[0][0]  # Three of a Kind
    if value_counts.most_common(2)[0][1] == 2 and value_counts.most_common(2)[1][1] == 2:
        return 3, [value_counts.most_common(1)[0][0], value_counts.most_common(2)[0][0]]  # Two Pair
    if value_counts.most_common(1)[0][1] == 2:
        return 2, value_counts.most_common(1)[0][0]  # One Pair
    return 1, sorted_values  # High Card


def compare_hands(hand1: list, hand2: list) -> int:
    """
    Compare two poker hands and return the winner.

    Parameters:
    hand1 (list): A list of strings representing the first poker hand.
    hand2 (list): A list of strings representing the second poker hand.

    Returns:
    int: The result of the comparison: 1 if hand1 wins, 2 if hand2 wins, 0 if tie.
    """
    rank1, value1 = evaluate_hand(hand1)
    rank2, value2 = evaluate_hand(hand2)

    if rank1 != rank2:
        return 1 if rank1 > rank2 else 2

    if isinstance(value1, list) and isinstance(value2, list):
        return 1 if value1 > value2 else 2 if value1 < value2 else 0
    return 1 if value1 > value2 else 2 if value1 < value2 else 0


if __name__ == "__main__":
    start_time = time.time()
    winner_count = sum(1 for line in open('Problem_54\\0054_poker.txt')
                       if compare_hands(*[line.strip().split()[i:i+5] for i in (0, 5)]) == 1)
    print(f'Answer = {winner_count}')
    print(f'Elapsed time: {round(time.time() - start_time, 2)} seconds')

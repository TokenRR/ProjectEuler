import time
import random
from typing import List


def monopoly(turns: int) -> List[int]:
    """
    Simulate the Monopoly game for a given number of turns.

    Args:
        turns (int): The number of turns to simulate.

    Returns:
        List[int]: A list representing the frequency of landing on each square.
    """
    squares, doubles, cc_i, ch_i, pos = [0] * BOARD_SIZE, 0, 0, 0, 0

    for _ in range(turns):
        die1, die2 = random.randint(1, DICE_SIDES), random.randint(1, DICE_SIDES)
        roll = die1 + die2
        doubles = 0 if die1 != die2 else doubles + 1

        if doubles >= 3:
            pos, doubles = JAIL, 0
        else:
            pos = (pos + roll) % BOARD_SIZE

            if pos == 30:  # G2J
                pos = JAIL
            elif pos in [2, 17, 33]:  # CC
                card = CC[cc_i]
                cc_i = (cc_i + 1) % len(CC)
                pos = card if card is not None else pos
            elif pos in [7, 22, 36]:  # CH
                card = CH[ch_i]
                ch_i = (ch_i + 1) % len(CH)
                if card is not None:
                    pos = process_card(pos, card)

        squares[pos] += 1

    return squares


def process_card(pos: int, card) -> int:
    """
    Process the CH card and update the current position.

    Args:
        pos (int): The current position on the board.
        card: The CH card.

    Returns:
        int: The updated position after processing the card.
    """
    if card == BACK_3:
        return (pos - 3) % BOARD_SIZE
    elif card == R:
        while pos not in R:
            pos = (pos + 1) % BOARD_SIZE
    elif card == U:
        while pos not in U:
            pos = (pos + 1) % BOARD_SIZE
    else:
        pos = card
    return pos


if __name__ == "__main__":
    start_time = time.time()

    # Constants
    BOARD_SIZE = 40
    DICE_SIDES = 4
    N = 1000000

    # Squares
    GO, JAIL, C1, E3, H2, R1 = 0, 10, 11, 24, 39, 5
    R, U, BACK_3 = [5, 15, 25, 35], [12, 28], -3

    # Cards
    CC = [GO, JAIL] + [None] * 14
    CH = [GO, JAIL, C1, E3, H2, R1, R, R, U, BACK_3] + [None] * 6

    # Shuffle the decks
    random.shuffle(CC)
    random.shuffle(CH)

    squares = monopoly(N)
    modal_string = ''.join(str(i) for i in sorted(range(BOARD_SIZE), key=lambda i: -squares[i])[:3])

    print(f"Answer = {modal_string}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")

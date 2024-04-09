import time
from math import gcd
from collections import Counter
from typing import List, Dict


def generate_pythagorean_triples(limit: int) -> List[int]:
    """
    Generate Pythagorean triples with perimeter less than or equal to the limit
    """
    triples: List[int] = []
    m_limit: int = int((limit // 2)**0.5)
    for m in range(2, m_limit):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a: int = m**2 - n**2
                b: int = 2 * m * n
                c: int = m**2 + n**2
                p: int = a + b + c
                while p <= limit:
                    triples.append(p)
                    p += a + b + c
    return triples


def count_unique_triples(limit: int) -> int:
    """
    Count the number of unique Pythagorean triples with perimeter less than or equal to the limit
    """
    triples: List[int] = generate_pythagorean_triples(limit)
    perimeter_counts: Dict[int, int] = Counter(triples)
    return sum(1 for p in perimeter_counts if perimeter_counts[p] == 1)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {count_unique_triples(1_500_000)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")

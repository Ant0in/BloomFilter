
from .universal_hash import UniversalHash
import random
from typing import Optional


class HashFactory:

    """Factory class to create universal hash functions."""

    @staticmethod
    def create(m: int, seed: Optional[int] = None) -> UniversalHash:

        """
        Create a new hash function with the given parameters. \n
        - **m** `(int)`: The size of the hash table.
        - **seed** `(Optional[int])`: An optional seed for the random number generator.
        """

        rnd: random.Random = random.Random(seed)
        p: int = (1 << 61) - 1
        a: int = rnd.randint(1, p - 1)
        b: int = rnd.randint(0, p - 1)
        return UniversalHash(p, a, b, m)


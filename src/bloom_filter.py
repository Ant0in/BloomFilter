
from __future__ import annotations

from .universal_hash import UniversalHash
from .hash_factory import HashFactory

from bitarray import bitarray
from typing import List, Optional



class BloomFilter:

    """A simple Bloom filter implementation using universal hash functions."""

    def __init__(self, m: int, hash_functions: List[UniversalHash]) -> None:

        """
        Initialize the Bloom filter with given parameters.
        - **m** `(int)`: Size of the bit array.
        - **hash_functions** `(List[UniversalHash])`: List of hash functions to use.
        """

        # Initialize parameters for the Bloom filter
        self._m: int = m
        self._k: int = len(hash_functions)
        self._hf: List[UniversalHash] = hash_functions

        # We use bit array but it's python so honestly who cares
        self._bit_array: bitarray = bitarray([0] * m)

    @classmethod
    def New(cls, m: int, k: int, seed: Optional[int] = None) -> BloomFilter:

        """
        Create a new Bloom filter with `k` universal hash functions. \n
        Please refer to the `HashFactory` class for more details on the hash functions.
        """

        hash_functions: List[UniversalHash] = [
            HashFactory.create(m, seed + i if seed is not None else None)
            for i in range(k)
        ]

        return cls(m, hash_functions)

    def add(self, x: int) -> None:

        """Add an element to the Bloom filter using the provided hash functions."""

        # Compute which indices are going to be set to 1
        indices: List[int] = [hf(x) % self._m for hf in self._hf]

        for index in indices:
            self._bit_array[index] = 1

    def query(self, x: int) -> bool:

        """Check if an element is possibly in the Bloom filter using the provided hash functions."""

        # Compute which indices to check
        indices: List[int] = [hf(x) % self._m for hf in self._hf]

        # If all bits at these indices are 1, then x is possibly in the set
        # It might very well be a false positive.
        # However, if any bit is 0, then x is definitely not in the set.
        return all(self._bit_array[index] for index in indices)

    def __len__(self) -> int:
        """Return the size of the bit array."""
        return self._m

    def clear(self) -> None:
        """Clear the Bloom filter by resetting all bits to 0."""
        self._bit_array.setall(0)


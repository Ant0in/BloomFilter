

class UniversalHash:

    """A simple universal hash function for integers."""

    def __init__(self, p: int, a: int, b: int, m: int):
        
        """
        Initialize the hash function with given parameters.
        - **p** `(int)`: A large prime number.
        - **a** `(int)`: A random integer in the range **[1, p-1]**.
        - **b** `(int)`: A random integer in the range **[0, p-1]**.
        - **m** `(int)`: The size of the hash table.
        """

        self._p: int = p
        self._a: int = a
        self._b: int = b
        self._m: int = m

    def hash_int(self, value: int) -> int:

        """
        Hash an integer value. \n
        Raises a `ValueError` if the value is negative.
        """

        if value < 0:
            raise ValueError(f"[E] Value must be non-negative (got {value}).")

        return ((self._a * value + self._b) % self._p) % self._m

    def __call__(self, value: int) -> int:

        """Call the `hash_int` method on an integer value."""

        return self.hash_int(value)

    def __repr__(self) -> str:

        """Return a string representation of the hash function."""

        return f"UniversalHash(p={self._p}, a={self._a}, b={self._b}, m={self._m})"


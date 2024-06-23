from pipe import Pipe


class MinPQ:
    """Min heap priority queue for the Pipe class."""

    def __init__(self, size: int=10):
        """Initializes the MinPQ with the given size."""
        self.q = [None] * (size + 1)
        self.n = 0

    def isEmpty(self) -> bool:
        """Returns true if empty, else false."""
        return self.n == 0
    
    def isFull(self) -> bool:
        """Returns true if full, else false."""
        return self.n + 1 == len(self.q)
    
    def size(self) -> int:
        """Returns the size of the MinPQ."""
        return self.n
    
    def insert(self, pipe: Pipe) -> None:
        """Inserts the given pipe in the MinPQ if not full."""
        if self.isFull(): return
        self.n += 1
        self.q[self.n] = pipe
        self.swim(self.n)

    def min(self) -> Pipe:
        """Returns Pipe with the minimun count if not empty, else None."""
        return None if self.isEmpty() else self.q[1]
    
    def delMin(self) -> None:
        """Removes the minimum key."""
        if self.isEmpty(): return
        self.q[1] = self.q[self.n]
        self.n -= 1
        self.sink(1)

    def swim(self, k: int) -> None:
        """Swims the key to the top."""
        while k > 1:
            j = k // 2
            if self.q[j].count > self.q[k].count:
                self.q[k], self.q[j] = self.q[j], self.q[k]
            else:
                break
            k = j

    def sink(self, k: int) -> None:
        """Sinks the key to the bottom."""
        while k * 2 <= self.n:
            j = k * 2
            if j < self.n and self.q[j].count > self.q[j+1].count:
                j += 1
            if self.q[j].count < self.q[k].count:
                self.q[k], self.q[j] = self.q[j], self.q[k]
            else:
                break
            k = j
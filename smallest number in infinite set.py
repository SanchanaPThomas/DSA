import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.heap = []
        self.inheap = set()

    def popSmallest(self) -> int:
        # Case 1: If heap has elements, pop the smallest one
        if self.heap:
            val = heapq.heappop(self.heap)
            self.inheap.remove(val)
            return val     # ✅ return immediately

        # Case 2: Otherwise, take from the infinite sequence
        val = self.cur
        self.cur += 1
        return val

    def addBack(self, num: int) -> None:
        # Only add numbers that were previously popped and are not already in heap
        if num < self.cur and num not in self.inheap:
            heapq.heappush(self.heap, num)
            self.inheap.add(num)

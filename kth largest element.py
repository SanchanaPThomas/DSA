import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)  # add to heap
            if len(heap) > k:          # keep size at most k
                heapq.heappop(heap)
        return heap[0]  # smallest in heap = kth largest in array

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []

        for n, freq in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, n))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, n))

        return [n for freq, n in heap]


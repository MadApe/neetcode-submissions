class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            # push the negated number value (to force max to the top) and the index
            heapq.heappush(heap, (-nums[i], i))

            # when the heap size is at least k in length
            if i >= k - 1:
                # pop off k - 1 heap items, leaving the next item on the heap as the max
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)

                # reverse the negated value we created to force a max heap
                res.append(-heap[0][0])
        
        return res
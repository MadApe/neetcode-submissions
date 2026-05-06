class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k

        iterations = len(nums) - k + 1

        window_maxes = [0] * len(nums)
        # qs = []
        q = collections.deque()

        while l < len(nums):
            q.append(nums[l])
            if len(q) > k:
                q.popleft()

            # print(q)

            window_maxes[l] = max(q)
            l += 1


        return window_maxes[k-1:]
        


            




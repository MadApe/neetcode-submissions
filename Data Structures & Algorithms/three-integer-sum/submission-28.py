class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort so we can reduce this to a two pointer problem
        triplets = []  # track the unique triplets

        # we loop over the first N -2 elements.  i becomes the "anchor" and
        # for each anchor we use a two pointer approach to find complements
        # to the anchor
        for i in range(len(nums) - 2):
            n = nums[i]  # array value in the anchor position

            if n > 0:
                # if the anchor value is greater than zero there will be no other triplets
                # adding up to zero (since the array is sorted) so we can break early
                break

            # if the value of our current anchor is the same as the previous anchor
            # we skip it else it would result in duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            l = i + 1  # left pointer starts as element after the anchor
            r = len(nums) - 1  # right element starts at the end of the list

            # we'll move pointers inward looking for complements and stop when the left and right
            # pointers meet
            while l < r:
                ln = nums[l]
                rn = nums[r]
                summed = n + ln + rn

                # if anchor + left number + right number == 0 (condition satisfied), record it and
                # move both pointers inward.  As we move the pointers inward we want to keep moving
                # each respective pointer inward until we find a new value as processing a duplicate
                # value as the previous will result in duplicate triplets
                if summed == 0:
                    values = [n, ln, rn]
                    l += 1
                    r -= 1
                    triplets.append(values)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif summed < 0:
                    # the summed value is still less than zero so move the left pointer inward
                    l += 1
                else:
                    # summed value is greater than 0 so move the right pointer inward
                    r -= 1


        return triplets

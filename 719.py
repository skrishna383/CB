class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance):
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:  # move fast pointer
                    j += 1
                count += j - i - 1  # count pairs
                i += 1  # move slow pointer
            return count >= k

        nums.sort()
        n = len(nums)
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mi = l + (r - l) // 2
            if enough(mi):
                r = mi
            else:
                l = mi + 1
        return l

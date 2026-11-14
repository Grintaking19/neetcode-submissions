class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
            if i == len(nums) - 1:
                return i + 1


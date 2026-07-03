class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = {}
        for num in nums:
            if num in hashset:
                return num
            hashset[num] = 1
        return -1
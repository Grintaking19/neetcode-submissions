class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr_nums = [num**2 for num in nums]
        sqr_nums.sort()
        return sqr_nums
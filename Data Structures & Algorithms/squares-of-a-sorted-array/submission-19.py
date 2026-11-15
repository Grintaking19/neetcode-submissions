class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # edge cases
        if not nums:
            return nums
        if len(nums) == 1:
            return [nums[0]**2]
        if nums[0] > 0:
            return [num**2 for num in nums]
        
        pivot = 0
        while  pivot < len(nums) and nums[pivot] < 0:
            pivot +=1
        
        if pivot == len(nums):
            return [num ** 2 for num in nums[::-1]]
        
        left = pivot - 1
        res = []
        while left >= 0 and pivot < len(nums):
            if abs(nums[left]) < abs(nums[pivot]):
                res.append(nums[left])
                left -=1
            else:
                res.append(nums[pivot])
                pivot +=1
        if left >= 0:
            res.extend(nums[left::-1])
        elif pivot < len(nums):
            res.extend(nums[pivot:])
        
        return [num**2 for num in res]


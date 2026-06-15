class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[i] + numbers[mid] == target:
                    return [i+1, mid+1]
                elif numbers[i] + numbers[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
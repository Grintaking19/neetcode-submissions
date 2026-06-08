class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_index_map :
                return [min(i, num_index_map[diff]), max(i, num_index_map[diff])]
            num_index_map[n] = i
        return []
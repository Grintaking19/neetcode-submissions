class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unqiue = set()
        for num in nums:
            if num not in unqiue:
                unqiue.add(num)
            else:
                return True

        return False
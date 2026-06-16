class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        max_height = max(heights)
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(area, max_area)
            if heights[r] > heights[l]:
                l +=1
            else:
                r -=1
            if max_area > max_height * (r-l):
                break            
        return max_area
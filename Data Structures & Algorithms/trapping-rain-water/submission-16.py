class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        stack = []
        trapped_water = 0 
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    left = height[i]
                    right = height[stack[-1]]
                    h = min(left, right) - mid
                    w = i - stack[-1] - 1
                    trapped_water += h * w
            stack.append(i)

        return trapped_water
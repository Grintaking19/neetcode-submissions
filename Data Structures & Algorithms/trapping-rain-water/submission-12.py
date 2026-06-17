class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix sum
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        res = 0
        for i in range(n):
            if i == 0:
                leftMax[i] = height[i]
                continue
            leftMax[i] = max(leftMax[i-1], height[i])
        
        for i in range(n-1,-1,-1):
            if i == n-1:
                rightMax[i] = height[i]
                continue
            rightMax[i] = max(rightMax[i+1], height[i])

        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]


        return res
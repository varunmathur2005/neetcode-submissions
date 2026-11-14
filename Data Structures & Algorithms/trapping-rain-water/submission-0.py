class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        leftMax = [0] * n
        leftMax[0] = height[0]
        rightMax = [0] * n
        rightMax[-1] = height[-1]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        for j in range(n - 2, -1, -1):
            rightMax[j] = max(rightMax[j + 1], height[j])
        
        for i, h in enumerate(height):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res
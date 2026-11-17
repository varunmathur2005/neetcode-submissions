class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Store the heights underconsideration
        stack = [] # (start, height)

        maxArea = 0

        for i, h in enumerate(heights):
            # Cannot extend height further
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)    
                start = index
            
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
        

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(height, index)
        maxArea = 0
        for curI, curH in enumerate(heights):
            left_Index = curI
            while stack and curH <= stack[-1][0]:
                height, indx = stack.pop()
                area = height * (curI - indx)
                maxArea = max(maxArea, area)
                left_Index = indx
            stack.append((curH, left_Index))

        n = len(heights)
        for h, i in stack:
            area = h * (n - i)
            maxArea = max(maxArea, area)
        return maxArea
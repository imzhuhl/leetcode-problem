"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入: [2,1,5,6,2,3]
输出: 10
"""
from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            wid = i - stack[-2] - 1
            hei = heights[stack[-1]]
            max_area = max(max_area, wid * hei)
            stack.pop()
        stack.append(i)
            
    while stack[-1] != -1:
        wid = len(heights) - stack[-2] - 1
        hei = heights[stack[-1]]
        max_area = max(max_area, wid * hei)
        stack.pop()

    return max_area

if __name__ == "__main__":
    heights = [2, 1, 2]
    print(largestRectangleArea(heights))

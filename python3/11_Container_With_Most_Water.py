from typing import List
import pdb


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            if height[left] >= height[right]:
                area = max(area, (right - left) * height[right])
                right -= 1
            else:
                area = max(area, (right - left) * height[left])
                left += 1
        return area
            

if __name__ == "__main__":
    lst = [1, 1]
    print(Solution().maxArea(lst))

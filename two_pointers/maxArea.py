from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        start = 0
        end = len(heights)-1
        while start<end:
            area = (end - start)*min(heights[start], heights[end])
            if heights[start] <= heights[end]:
                start += 1
            else: 
                end -= 1 
            res = max(res, area)
        return res 
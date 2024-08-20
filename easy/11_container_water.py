from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        for i in range(n):
            for j in range(n-1):
                lower_height = min(height[i], height[j + 1])
                distance = j + 1 - i 
                new_max = distance * lower_height
                max_water = new_max if new_max > max_water else max_water
        return max_water




height = [1,8,6,2,5,4,8,3,7]
output = 49

water = Solution()
print (water.maxArea([1,8,6,2,5,4,8,3,7]), 49)
print (water.maxArea([1,1]), 1)
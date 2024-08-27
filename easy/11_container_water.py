from typing import List


class Solution1:
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


class Solution:
    '''
    https://www.pluralsight.com/resources/blog/guides/algorithm-templates-two-pointers-part-2
    '''
    def left_condition(self, left):
        pass

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        while left < right:
            if self.left_condition(left):
                left += 1
            if self.right_condition(right):
                right -= 1
            self.process_logic(left, right)



height = [1,8,6,2,5,4,8,3,7]
output = 49

water = Solution()
print (water.maxArea([1,8,6,2,5,4,8,3,7]), 49)
print (water.maxArea([1,1]), 1)
from typing import List


class Solution1:
    def maxArea(self, height: List[int]) -> int:
        # array ---- [a, b, c,]
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
    def left_condition(self, height, left, right):
        if height[left] < height[right]:
            return True
        else:
            return False

    def right_condition(self, right):
        pass

    def process_logic(self, height, left, right, max_area):
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        return max_area
        

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            max_area = self.process_logic(height, left, right, max_area)

            if self.left_condition(height, left, right):
                left += 1
                print('move left pointer forward')
            else:
                print('move right pointer backward')
                right -= 1

        return max_area



height = [1,8,6,2,5,4,8,3,7]
output = 49

water = Solution()
print (water.maxArea([1,8,6,2,5,4,8,3,7]), 49)
print (water.maxArea([1,1]), 1)
from typing import List, Tuple

class Solution:
    def calculate_area(self, height: List[int], i: int, j: int) -> float:
        """
        Calculate the area between lines at index i and j.
        The area consists of a rectangle and two triangles.
        """
        rectangle_area = min(height[i], height[j]) * (j - i)
        triangle_area = 0.5 * abs(height[i] - height[j]) * (j - i)
        total_area = rectangle_area + triangle_area
        return total_area

    def calculate_flow_rate(self, height: List[int], i: int, j: int) -> float:
        """
        Calculate the flow rate between lines at index i and j.
        Flow rate is the absolute difference in height divided by the distance.
        """
        return abs(height[j] - height[i]) / abs(j - i)
    
    def left_condition(self, height, left, right):
        if height[left] < height[right]:
            return True
        else:
            return False
        
    def process_logic(self, height, left, right, max_area):
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        return max_area


    def maxAreaWithFlowRate(self, height: List[int]) -> Tuple[List[int], float, float]:
        left = 0
        right = len(height) - 1
        max_area = 0
        max_flow_rate = 0
        best_pair = []
        max_total = 0

        while left < right:
            # Calculate the area and flow rate for the current pair
            current_area = self.calculate_area(height, left, right)
            current_flow_rate = self.calculate_flow_rate(height, left, right)
            current_total = current_flow_rate + current_area

            print(current_total, max_total, left, height[left], right, height[right])
            if current_total > max_total:
                max_total = max(current_total, max_total)
                best_pair = [left, right]
            

            # Check if this is the best pair we've seen
            # if current_area > max_area or (current_area == max_area and current_flow_rate > max_flow_rate):
            #     max_area = current_area
            #     max_flow_rate = current_flow_rate
            #     best_pair = [left, right]

            # Move the pointers based on the height comparison
            if self.left_condition(height, left, right):
                left += 1
            else:
                right -= 1

        return best_pair

# Example Usage
solution = Solution()

# Example 1
height1 = [1,8,6,2,5,4,8,3,7]
print(solution.maxAreaWithFlowRate(height1))  # Output: [1, 8], area and flow rate

# Example 2
height2 = [5, 5, 5, 5]
print(solution.maxAreaWithFlowRate(height2))  # Output: [0, 3], area and flow rate

# Example 3
height3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(solution.maxAreaWithFlowRate(height3))  # Output: [0, 9], area and flow rate

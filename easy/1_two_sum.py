class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        arr = len(nums)
        first_index = 0
        second_index = 0
        while start < arr:
            for i in nums:
                if (nums[start] + i) == target and nums.index(i) != start:
                    first_index = start
                    second_index = nums.index(i)
                    return [first_index, second_index]

            start = start + 1
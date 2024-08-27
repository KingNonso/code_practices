from typing import List


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
        return []

    '''
    So, if we fix one of the numbers, say x, we have to scan the entire array 
    to find the next number y which is value - x where value is the input parameter. 
    Can we change our array somehow so that this search becomes faster?'''

    # A possible solution is to use a hash map (Python's dictionary) to store the values and their indices.
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)

        for i in range(len(nums)):
            hash_map[i] = nums[i]
        
        for i in nums:

            
        print(hash_map)



# Testcases
t = Solution()
print(t.twoSum2([2,7,11,15], 9))


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[j] = i

        for i, j in enumerate(nums):
            result = target - j 
            print(i, j, target, result, hashmap)
            if (target - j) in hashmap and hashmap[target - j] != i:
                return [i, nums.index(target - j)]
            

s = Solution()
print(s.twoSum([3,4,5,6], 7), "[0, 1]")
print(s.twoSum([4,5,6], 10), "[0, 2]")
print(s.twoSum([5,5], 10), "[0, 1]")

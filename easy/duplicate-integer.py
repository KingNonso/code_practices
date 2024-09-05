from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset = {}
         for i in nums:
              if i in hashset:
                   return True
              else:
                   hashset[i] = i
         
         return False
    

solution = Solution()
print(solution.hasDuplicate([1,2,3,3]), True)
print(solution.hasDuplicate([1,2,3,4]), False)


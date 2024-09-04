from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        
        s_hashmap = Counter(s)
        t_hashmap = Counter(t)

        if s_hashmap == t_hashmap:
            return True
        return False
        


s = "racecar"
t = "carrace"
problem = Solution()
print(problem.isAnagram(s, t), True)

s = "a"
t = "ab"
print(problem.isAnagram(s, t), False)




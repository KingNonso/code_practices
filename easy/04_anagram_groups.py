from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # take the list item and loop over it
        # in each loop, sort it first and hash it
        # if it exists put it in a hashmap of likes
        # hashmap = {}
        # output = []
        # for j, i in enumerate(strs):
        #     sorted_i = sorted(i)
        #     if sorted_i in hashmap:
        #         output.insert(j, i)
        #         output[hashmap[sorted_i]] = i
        #     hashmap[sorted_i] = j
            
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # maps a - z
            for c in s:
                count[ord(c) - ord("a")] += 1
                print(count)
            res[tuple(count)].append(s)
            print(res)
        return res.values()
        

strs = ["act","pots","tops","cat","stop","hat"]

output = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

s = Solution()
result = s.groupAnagrams(strs)
print(result is output, result)

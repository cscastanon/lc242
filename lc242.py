#LeetCode 242
# Valid Anagram
# Diff: Easy
#Time Complexity: O(n)
#Space Complex: O(2n) => O(n)

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        hS, hT = {}, {}

        for c in range(len(s)):
            hS[s[c]] = 1 + hS.get(s[c], 0)
        
        for c in t:
            hT[c] = 1 + hT.get(c, 0)
        
        return True if hS == hT  else False
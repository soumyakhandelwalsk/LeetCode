#Problem: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        dictionary = {'(':')','{':'}','[':']'}
        for i in s:
            if i in ['(','{','[']:
                ls.append(i)
            elif len(ls)==0 or dictionary[ls.pop()]!=i:
                return False
        return len(ls)==0

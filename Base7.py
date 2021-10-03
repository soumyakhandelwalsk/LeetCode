#Problem: https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        q = num
        s = ""
        neg = False
        if num<0:
            neg = True
            q = (-1)*num
        while(q>0):
            s = str(q%7) + s
            q = q//7
        if neg:
            s = "-"+s
        return s

#Problem: https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        s = (l*(l+1))>>1
        for i in nums:
            s = s - i
        return s

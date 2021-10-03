#Problem: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1
        l = height[left]
        r = height[right]
        while(left<right):
            temp = min(l,r)*(right-left)
            if temp>area:
                area = temp
            if l<r:
                left +=1
                l = height[left]
            else:
                right -=1
                r = height[right]
        return area
        

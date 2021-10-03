#Problem: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rest = head
        tail = None
        while(rest!=None):
            rest = head.next
            head.next = tail
            tail = head
            head = rest         
        return tail

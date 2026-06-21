# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_dict = {}
        dummy = head
        count = 0
        while head:
            if head not in visited_dict:
                visited_dict[head] = count
                count +=1
                head = head.next
            else:
                return True
        return False
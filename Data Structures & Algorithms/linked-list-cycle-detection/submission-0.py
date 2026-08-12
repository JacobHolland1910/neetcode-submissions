# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        hashset = set()
        
        while curr:
            if curr.next not in hashset:
                hashset.add(curr.next)
                curr = curr.next
            else:
                return True

        return False


            
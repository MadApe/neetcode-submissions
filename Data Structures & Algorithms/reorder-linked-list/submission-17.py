# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        if len(nodes) == 1:
            return

        l = 0
        r = len(nodes) - 1

        while l < r:
            nodes[l].next = nodes[r]
            nodes[r].next = nodes[l+1]
            l += 1
            r -= 1

        nodes[l].next = None

        return
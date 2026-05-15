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

        reordered = []
        while l <= r:
            reordered.append(nodes[l])
            reordered.append(nodes[r])
            l += 1
            r -= 1


        for i in range(len(reordered) - 1):
            reordered[i].next = reordered[i+1]

        reordered[-1].next = None

        return
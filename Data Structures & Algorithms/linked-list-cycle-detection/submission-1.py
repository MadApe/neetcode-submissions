# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # this works because if fast or fast.next ever become null then
        # it hit the end of the linked list without cycling.
        # if there is a cycle the only way it will exit the loop is when
        # the slow and fast pointers eventually point at the same node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


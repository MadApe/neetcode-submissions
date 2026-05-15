# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev_node = None
        next_node = None
        node = head

        while node.next:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
            

        # print(f"node_val={node.val}, node_next={node.next}")

        node.next = prev_node

        return node

            
            

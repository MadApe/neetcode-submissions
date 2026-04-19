# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2

        if not l2:
            return l1

        answer: ListNode = None
        l1_ptr = l1
        l2_ptr = l2
        carry = 0
        current_ans_node = None
        previous_ans_node = None

        while l1_ptr or l2_ptr:
            l1_val = l1_ptr.val if l1_ptr else 0
            l2_val = l2_ptr.val if l2_ptr else 0
            sum_val = l1_val + l2_val + carry

            digit = sum_val % 10
            carry = sum_val // 10

            # print(f"l1_val: {l1_val}, l2_val: {l2_val}, carry: {carry}, digit: {digit}, sum_val: {sum_val}")

            current_ans_node = ListNode(val=digit)
            if not answer:
                answer = current_ans_node

            if previous_ans_node:
                previous_ans_node.next = current_ans_node

            previous_ans_node = current_ans_node

            l1_ptr = l1_ptr.next if l1_ptr else None
            l2_ptr = l2_ptr.next if l2_ptr else None

        if carry:
            current_ans_node = ListNode(val=carry)
            if previous_ans_node:
                previous_ans_node.next = current_ans_node

        # next_node = answer
        # while next_node:
            # print(f"next_node={next_node}, next_node.val = {next_node.val}, next_node.next = {next_node.next}")
            # next_node = next_node.next

        return answer


        

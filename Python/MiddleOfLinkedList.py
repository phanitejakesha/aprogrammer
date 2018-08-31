#Given a non-empty, singly linked list with head node head,
#return a middle node of linked list
#If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        ptr1 = head #pointer which moves two nodes
        ptr2 = head #pointer which moves one node
        while ptr1 and ptr1.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next.next
        return ptr2



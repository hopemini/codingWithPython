# Definition for singly-linked list.
from typing import List


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    result = ListNode(-1)
    head = result
    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next
    if list1 != None:
        head.next = list1
    else:
        head.next = list2
    return result.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = mergeTwoLists(l1, l2)
while l3 != None:
    print(l3.val)
    l3 = l3.next
# LEETCODE #0002



# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = ""
        s2 = ""
        
        while l1 is not None:
            s1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2 += str(l2.val)
            l2 = l2.next
        
        s1,s2 = (s1[::-1], s2[::-1])
        
        res = int(s1) + int(s2)

        res = str(res)[::-1]
        
        l3 = ListNode(int(res[0]))
        current = l3
        
        for i in range(1, len(res)):
            current.next = ListNode(int(res[i])) 
            current = current.next

        return l3

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))

print(Solution().addTwoNumbers(l1,l2).val)
print(Solution().addTwoNumbers(l1,l2).next.val)
print(Solution().addTwoNumbers(l1,l2).next.next.val)

print(ListNode(7,ListNode(0,ListNode(8))).val)
print(ListNode(7,ListNode(0,ListNode(8))).next.val)
print(ListNode(7,ListNode(0,ListNode(8))).next.next.val)

assert Solution().addTwoNumbers(l1,l2) == ListNode(7,ListNode(0,ListNode(8)))
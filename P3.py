# LEETCODE #0027

# Given an integer array nums and an integer val, remove all occurrences of 
#   val in nums in-place. The order of the elements may be changed. Then return
#   the number of elements in nums which are not equal to val.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for a in nums[::-1]:     
            if a == val:
                nums.remove(val)   
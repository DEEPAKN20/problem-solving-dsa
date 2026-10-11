# https://leetcode.com/problems/first-unique-even-element/description/
# https://leetcode.com/submissions/detail/2169020285/

# 11 October 2026 - 20 Mins

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        arr=[]
        for i in nums:
            if i%2==0 and nums.count(i)==1:
                return i
                break
        else:
            return -1

"""
we use break because it after printing first element i it Breaks
"""
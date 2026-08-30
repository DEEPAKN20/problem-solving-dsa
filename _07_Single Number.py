#https://leetcode.com/problems/single-number/description/
#https://leetcode.com/problems/single-number/submissions/2124736946/
# 30 August 2026
# Solution using XOR

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for x in nums:
            result = result ^ x

        return result

#https://leetcode.com/problems/single-number/submissions/2124726536/
# Solution using count()

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for i in nums:
            if nums.count(i)==1:
                return i
                
"""
"""

        
        
        
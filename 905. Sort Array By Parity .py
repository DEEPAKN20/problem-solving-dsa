# https://leetcode.com/problems/sort-array-by-parity/description/
# https://leetcode.com/submissions/detail/2169322161/

# 11 October 2026 - 15 Mins

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort()
        result=even+odd
        return(result)
"""

"""
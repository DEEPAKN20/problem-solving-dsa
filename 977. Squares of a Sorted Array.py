# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# https://leetcode.com/submissions/detail/2159544726/

# 02 October 2026 - 10 Mins

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result=[]
        x=sorted(nums,key=abs)
        for i in range(len(x)):
            y=result.append(x[i]**2)
        return(result)


""" abs gives the absolute value os an integer

"""

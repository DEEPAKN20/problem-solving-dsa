#https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
#https://leetcode.com/submissions/detail/2146576672/

# 19 September 2026 - 30 Mins 

class Solution:
    def sumOfSquares(self, nums):
        n = len(nums)
        result = 0

        for i in range(n):
            if n % (i + 1) == 0:
                result +=(nums[i]*nums[i])

        return result

"""

"""
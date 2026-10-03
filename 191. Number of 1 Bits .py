#https://leetcode.com/problems/number-of-1-bits/description/
#https://leetcode.com/submissions/detail/2146910135/

# 19 September 2026 - 10 Mins

class Solution:
    def hammingWeight(self, n: int) -> int:
        x=[]
        binary=bin(n)[2:]
        x+=binary
        return(x.count('1'))

"""

"""
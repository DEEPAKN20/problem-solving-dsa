#https://leetcode.com/problems/smallest-even-multiple/description/
#https://leetcode.com/submissions/detail/2154186589/

#26 September 2026 - 5 Mins

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            return n*2

"""

"""
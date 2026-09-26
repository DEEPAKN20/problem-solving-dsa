#https://leetcode.com/problems/richest-customer-wealth/description/
#https://leetcode.com/submissions/detail/2154194716/

#26 September 2026 - 5 Mins

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        x=[]

        for account in accounts:
            y=x.append(sum(account))
        return(max(x))

"""

"""
                
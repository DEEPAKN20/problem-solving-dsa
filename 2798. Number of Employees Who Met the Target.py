#https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
#https://leetcode.com/submissions/detail/2153186548/

# 25 September 2026 - 10 Mins

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        rs=[]
        for i in hours:
            if i>=target:
                y=rs.append(i)
            
        return(len(rs))

"""
"""


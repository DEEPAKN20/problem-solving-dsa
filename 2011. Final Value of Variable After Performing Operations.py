#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
#https://leetcode.com/submissions/detail/2154234541/

#26 September 2026  - 5 Mins

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x=0
        for i in operations:
            if "++" in i:
                x+=1
            else:
                x-=1
        return x


"""

"""
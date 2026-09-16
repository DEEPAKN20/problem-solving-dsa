#https://leetcode.com/problems/count-operations-to-obtain-zero/description/
#https://leetcode.com/submissions/detail/2143818265/

# 16 September 2026 - 20 Mins

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        step=0
        while num1!=0 and num2!=0:
            if num1>=num2:
                num1=num1-num2
            else:
                num2=num2-num1
            step+=1
        return step
        

"""
count += 1 means increase count by 1.
count = 0

# 2 operations happen
count += 1   # count = 1
count += 1   # count = 2
"""
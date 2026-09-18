#https://leetcode.com/problems/sum-of-unique-elements/description/
#https://leetcode.com/submissions/detail/2145738710/

# 18 September 2026 - 10 Mins

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        x=[]
        for i in nums:
            if nums.count(i)==1:
                x.append(i)
        return(sum(x))

"""

"""
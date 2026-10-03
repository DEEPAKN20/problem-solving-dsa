#https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/2158402763/


# 30 September 2026 - 30 Mins

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen=set()
        result=[]
        for i in nums:
            if i in seen:
                result.append(i)
        
            else:
                seen.add(i)

        return result


class Solution: #Time Limit Exceeded
    def findDuplicates(self, nums: list[int]) -> list[int]:
        x=[]
        for i in nums:
            if nums.count(i)>1:
                y=x.append(i)
        return(list(set(x)))

"""

"""
                
        
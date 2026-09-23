#https://leetcode.com/problems/single-number-iii/description/
#https://leetcode.com/problems/single-number-iii/submissions/2151065705/

#23 September 2026 - 10 Mins

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        y=[]
        for i in nums:
            if nums.count(i)==1:
                y.append(i)
        return y

    """
    Check in Better approach
    
    """
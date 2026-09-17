#https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
#https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/submissions/2144717385/ -Solution 1
#https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/submissions/2144722653/ -Solution 2

#17 September 2026 - 40Mins


#Solution 1
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        result=[]
        Avg=[]
        for i in nums:
            if i % 2 == 0:
                result.append(i)
        for i in result:
            if i%3==0:
                Avg.append(i)
        if len(Avg)==0:
            return 0
        return(sum(Avg)//len(Avg))

    # Solution 2
    class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sm , step = 0 , 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sm += i
                step += 1
        if step == 0:
            return 0
        return sm // step 

    """
    """
        
                
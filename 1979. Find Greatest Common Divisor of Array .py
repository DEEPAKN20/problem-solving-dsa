#https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

#https://leetcode.com/problems/find-greatest-common-divisor-of-array/submissions/2141250578/
#https://leetcode.com/problems/find-greatest-common-divisor-of-array/submissions/2141255709/

# 14 September 2026 - 25 Mins

# Solution 1
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        arr1=[]
        arr2=[]

        for i in range(1,x+1): #finding factors of x
            if x % i == 0:
                r=arr1.append(i)
        for i in range(1,y+1): #finding factors of y
            if y % i == 0:
                r=arr2.append(i)

        common=[]

        for i in arr1:
            if i in arr2:
                common.append(i)
        return max(common)

    # Solution 2
    class Solution:
        def findGCD(self, nums: List[int]) -> int:
            x=min(nums)
            y=max(nums)
            return gcd(x,y)


        
        
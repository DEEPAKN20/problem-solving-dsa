#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

#https://leetcode.com/submissions/detail/2139789990/

#12 September 2026 - 15 Mins

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ=0
        product=1
        while n>0:
            dig=n%10
            summ+=dig
            product*=dig
            n//=10
        return product-summ


"""

"""


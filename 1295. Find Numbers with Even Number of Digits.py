#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
#https://leetcode.com/submissions/detail/2143876715/

#16 September 2026 - 25 Mins

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result=[]
        for num in nums:
            if len(str(num)) % 2 == 0:
                result.append(num)
        return (len(result)) 



        """
        str() is used to convert a number into a string (text).
        If you don't use str(), Python treats the value as a number, not text:TypeError: object of type 'int' has no len()
        """
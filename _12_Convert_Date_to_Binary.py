#https://leetcode.com/problems/convert-date-to-binary/description/

#https://leetcode.com/submissions/detail/2140590575/

# 13 September 2026 - 35 mins

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year,month,day=date.split("-")
        def binary(n):
            n=int(n)
            result=""

            while n>0:
                rem=n%2
                result=str(rem)+result
                n//=2
            return result
        return binary(year)+"-"+ binary(month)+"-"+binary(day)
        

"""

"""
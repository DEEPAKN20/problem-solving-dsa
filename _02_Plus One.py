# https://leetcode.com/problems/plus-one/
# https://leetcode.com/problems/plus-one/description/
# 27 July 2026 - 45mins

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            for i in range(len(digits)-1,-1,-1):
                if digits[i]<9:
                    digits[i]+=1
                    return digits
                digits[i]=0
            return[1]+digits


            
                
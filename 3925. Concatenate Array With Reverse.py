#https://leetcode.com/problems/concatenate-array-with-reverse/description/

#https://leetcode.com/submissions/detail/2141593894/

#14 September 2026 - 5 Mins

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums1=nums[::-1]
        ans=nums+nums1
        return ans
        

        
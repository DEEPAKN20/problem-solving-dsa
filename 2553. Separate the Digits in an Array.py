# https://leetcode.com/problems/separate-the-digits-in-an-array/description/
# https://leetcode.com/submissions/detail/2162427764/

# 04 October 2026 -10 Mins

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            for digit in str(num):
                result.append(int(digit))

        return(result)


"""

"""
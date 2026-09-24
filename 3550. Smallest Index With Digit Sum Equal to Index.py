#https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/
#https://leetcode.com/submissions/detail/2152025165/

# 24 September 2026 - 15 Mins

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(map(int,str(nums[i]))) == i:
                return i
        return -1

    """
    sum(map(int,str(nums[i]))) == i:
    nums[i]              # get number
    str(nums[i])         # convert number → string
    map(int, ...)        # convert each digit → integer
    sum(...)             # add the digits
    == i                 # compare with i

    map() in Python is used to apply a function to every item in an iterable (like a list, string, tuple, etc.).
    """

        
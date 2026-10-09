# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/description/
# https://leetcode.com/submissions/detail/2167569958/

# 09 october 2026 - 30 Mins

class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        result=[]

        for num in nums:
            if freq[num] == 1 and num - 1 not in freq and num + 1 not in freq:
                result.append(num)
        return result

    """
    """

# TLE Time limit Exceeeded

class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        result=[]
        for num in nums:
            if nums.count(num)==1 and num-1 not in nums and num+1 not in nums:
                result.append(num)
        return result
"""

"""
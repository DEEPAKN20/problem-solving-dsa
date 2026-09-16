#https://leetcode.com/problems/majority-element-ii/description/
#https://leetcode.com/submissions/detail/2143844458/

# 16 September 2026 - 10 Mins

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count = {}
        result = []

        for m in nums:
            count[m] = count.get(m, 0) + 1

        for m in count:
            if count[m] > n // 3:
                result.append(m)

        return result

    """
    here first we want to create an empty list
    """

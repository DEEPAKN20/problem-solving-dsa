# https://leetcode.com/problems/compute-alternating-sum/description/
# https://leetcode.com/submissions/detail/2166336517/

# 08 October 2026 - 10 Mins

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            if i%2==0:
                result+=nums[i]
            else:
                result-=nums[i]
        return result

"""

"""
#https://leetcode.com/problems/maximum-subarray/description/
#https://leetcode.com/submissions/detail/2149743009/

#22 September 2026 - 35 Mins

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum=nums[0]
        maximum=nums[0]

        for i in range(1,len(nums)):
            current_sum=max(nums[i],current_sum+nums[i])
            maximum=max(maximum,current_sum)
        return maximum

"""

"""
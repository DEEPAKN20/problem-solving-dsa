# https://leetcode.com/problems/top-k-frequent-elements/description/
# https://leetcode.com/submissions/detail/2160299829/

# 2 October 2026 - 20 Mins

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result=[]
        for i in nums:
            if i not in result:
                result.append(i)
        result.sort(key=nums.count,reverse=True)
        return(result[:k])


"""

"""
# https://leetcode.com/problems/find-lucky-integer-in-an-array/
# https://leetcode.com/submissions/detail/2106806227/
# 14 August 2026 - 30 mins

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky=-1
        for num in arr:
            if arr.count(num)==num:
                lucky=max(lucky,num)
        return lucky


""" NOTES: 

""" 
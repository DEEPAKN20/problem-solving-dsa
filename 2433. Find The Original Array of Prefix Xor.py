#https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/
#https://leetcode.com/submissions/detail/2156023169/

# 28 September 2026 - 25 Mins

class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        result=[pref[0]]
        for i in range(1,len(pref)):
            result.append(pref[i]^pref[i-1])
        return result

"""

"""
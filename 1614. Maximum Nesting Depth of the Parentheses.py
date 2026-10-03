#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
#https://leetcode.com/submissions/detail/2156007761/

# 28  September 2026 - 25 Mins

class Solution:
    def maxDepth(self, s: str) -> int:
        ans=depth=0
        for ch in s:
            depth+=(ch=="(")-(ch==")")
            ans=max(ans,depth)
        return ans


"""

"""
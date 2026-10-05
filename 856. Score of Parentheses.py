# https://leetcode.com/problems/score-of-parentheses/description/?envType=daily-question&envId=2026-10-05
# https://leetcode.com/submissions/detail/2163287029/

# 05 October 2026 - 25 Mins

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        depth=0

        for i,ch in enumerate(s):
            if ch=="(":
                depth+=1
            else:
                depth-=1

                if s[i-1]=="(":
                    score +=1<<depth
        return score


"""
score +=1<<depth,it calulates the depth
depth = 0 → score = 1
inner () is at depth 1 → score = 2

"""
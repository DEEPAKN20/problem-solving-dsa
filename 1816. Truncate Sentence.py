#https://leetcode.com/problems/truncate-sentence/description/
#https://leetcode.com/submissions/detail/2153165167/

# 25 September 2026 - 5 Mins

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x=(s.split()[:k])
        return(" ".join(x))


"""

"""
#https://leetcode.com/problems/find-words-containing-character/description/
#https://leetcode.com/submissions/detail/2157293285/

# 29 September 2026 - 15 Mins

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        c=[]
        for i in range(len(words)):
            if x in words[i]:
                y=c.append(i)
        return c

"""

"""
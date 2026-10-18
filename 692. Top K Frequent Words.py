# https://leetcode.com/problems/top-k-frequent-words/description/
# https://leetcode.com/problems/top-k-frequent-words/submissions/

# 18 October 2026 - 20 Mins

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq={}
        for word in words:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        result=sorted(freq,key=lambda word:(-freq[word],word))
        return result[:k]

"""

"""

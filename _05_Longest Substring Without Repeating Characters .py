#https://leetcode.com/problems/longest-substring-without-rep
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# 26 August 2026 - 30 mins

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        for i in range(len(s)):
            current=""
            for j in range(i,len(s)):
                if s[j] in current:
                    break
                current+=s[j]
                longest=max(longest,len(current))

        return longest
    
        
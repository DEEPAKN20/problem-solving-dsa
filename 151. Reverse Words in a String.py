#https://leetcode.com/problems/reverse-words-in-a-string/description/
#https://leetcode.com/submissions/detail/2147724975/ - Solution 1
#https://leetcode.com/problems/reverse-words-in-a-string/submissions/2147724270/- Solution 2

class Solution: #Solution 1
    def reverseWords(self, s: str) -> str:
        x=s.split()
        y=" ".join(x[::-1])
        return y

class Solution: #Solution 2
    def reverseWords(self, s: str) -> str:
        x=s.split()
        y=" ".join(reversed(x))
        return y

        

        

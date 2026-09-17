#https://leetcode.com/problems/removing-stars-from-a-string/description/
#https://leetcode.com/submissions/detail/2144693125/

#17 September 2026 - 20 Mins

class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch != "*":
                stack.append(ch)
            else:
                stack.pop()
        return("".join(stack))

    """
    1." ".join(['a', 'b', 'c'])-join() = convert a list of strings/characters into one string.
    2.stack.pop()-Remove the last item from the stack.

    """
                
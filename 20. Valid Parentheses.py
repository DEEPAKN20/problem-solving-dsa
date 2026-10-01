#https://leetcode.com/problems/valid-parentheses/description/?envType=daily-question&envId=2026-10-01
#https://leetcode.com/submissions/detail/2159494615/

# 01 October 2026 - 35 Mins

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch =="(":
                stack.append(")")
            elif ch=="{":
                stack.append("}")
            elif ch=="[":
                stack.append("]")
            else:
                if not stack or stack.pop() != ch:
                    return False

        return len(stack) == 0

"""create an empty stack, check in given strings  ( { [ are present if yes then then append the exact opposite ] } ) to the stack.
After appending pop the each element from stack and check the popped element is equal to the given string if yes return true,else
false.And Finally check the stack length is empty.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack=[]
        for ch in s:
            if not stack or (ch == "(" or ch=="[" or ch=="{"):
                stack.append(ch)
            elif brackets.get(ch) == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return not stack
            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # store the opening brackets that have not been matched yet
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return (len(stack) == 0)
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for c in s:
            stack.append(c)
            if len(stack) > 1:
                pair = stack[-2] + stack[-1]
                if pair in ["AB", "CD"]:
                    stack.pop()
                    stack.pop()
                
        return len(stack)
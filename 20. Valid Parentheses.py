class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_brackets_stack = []

        brackets_pairs = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in brackets_pairs.values():
                open_brackets_stack.append(bracket)
            elif bracket in brackets_pairs:
                if not open_brackets_stack or open_brackets_stack.pop() != brackets_pairs[bracket]:
                    return False
            else:
                return False

        return not open_brackets_stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y,
                    "/": lambda x, y: int(x / y)
        }

        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[token](left, right))
            else:
                stack.append(int(token))

        return stack[-1]
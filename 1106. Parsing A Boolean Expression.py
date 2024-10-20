class Solution:
    def exp(self, exp: str, t: bool, f: bool) -> bool:
        if exp == "&":
            return t and not f
        if exp == "|":
            return t or not f
        
        
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for c in expression:
            if c in {"&", "|", "!", "t", "f"}:
                stack.append(c)
            elif c == ")":
                t = False
                f = False
                last = ""
                while stack[-1] in {"f", "t"}:
                    last = stack.pop()
                    if last == "t":
                        t = True
                    else:
                        f = True
                alg = stack.pop()
                if alg == "!":
                    stack.append("t" if last == "f" else "f")
                else:
                    stack.append("t" if self.exp(alg, t, f) else "f")

        return True if stack[0] == "t" else False
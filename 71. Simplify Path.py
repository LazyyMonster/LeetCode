class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splited_path = path.split("/")

        for part in splited_path:
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)

        return "/" + "/".join(stack)
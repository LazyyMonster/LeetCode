class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [0] * 10
        s = str(num)

        for d in s:
            digits[9 - int(d)] += 1

        left = 0
        digit = -1
        right = -1

        for d, f in enumerate(digits):
            c = 0
            if f != 0:
                for i in range(f):
                    if s[left] != str(9 - d):
                        break
                    left += 1
                    c += 1
                if c != f:
                    digit = 9 - d
                    break
        if left == len(s):
            return num

        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) == digit:
                right = i
                break

        res = s[:left] + str(digit) + s[left + 1: right] + s[left] + s[right + 1:]

        return int(res)

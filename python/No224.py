class Solution:
    def calculate(self, s: str) -> int:
        op = {1: lambda x, y: x + y,
              -1: lambda x, y: x - y}
        signs = [1, 1]
        res = 0
        cur = ""
        for si in s:
            if si == " ":
                continue
            if si.isdigit():
                cur += si
            else:
                if cur:
                    res = op[signs.pop(-1)](res, int(cur))
                    cur = ""
                if si == "+":
                    signs.append(signs[-1])
                elif si == "-":
                    signs.append(-signs[-1])
                elif si == "(":
                    signs.append(signs[-1])
                elif si == ")":
                    signs.pop(-1)
        if cur:
            res = op[signs.pop(-1)](res, int(cur))
            cur = ""
        return res
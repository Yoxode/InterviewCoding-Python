# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s: return ""
        return self.sol_1(s)

    def sol_1(self, s):
        s = list(s)
        status = 1
        while status:
            for i in range(len(s)):
                if s[i] == " ":
                    s[i] = "%20"
                    break
            if i == len(s) - 1:
                status = 0

        return "".join(s)
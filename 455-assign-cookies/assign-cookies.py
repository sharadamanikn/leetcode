class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()

        cookie_index=0
        for child_ind in range(len(g)):
            while cookie_index< len(s) and s[cookie_index]<g[child_ind]:
                cookie_index += 1
            if cookie_index >= len(s):
                return child_ind
            cookie_index += 1
        return len(g)


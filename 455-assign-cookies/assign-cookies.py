class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()

        count=0
        j=0
        i=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                count+=1
                j+=1
                i+=1
            else:
                j+=1
        return count


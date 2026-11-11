class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for item in strs:
            s="".join(sorted(item))
            d[s]=d.get(s,())+(item,)

        return list(d.values())
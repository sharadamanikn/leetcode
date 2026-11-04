class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        
        if len(s)!=len(t):
            return False

        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch]=1

        for ch in t:
            if ch not in s_dict or s_dict[ch]==0:
                return False
            else:
                s_dict[ch]=s_dict[ch]-1 #once a char is checked decrement its count.

        return True    
        

        
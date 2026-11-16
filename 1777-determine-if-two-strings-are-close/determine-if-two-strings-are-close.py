class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        set1=set(word1)
        set2=set(word2)
        if set1!=set2:
            return False
        
        freq_1={}
        freq_2={}

        for char in word1:
            if char not in freq_1:
                freq_1[char]=1
            freq_1[char] += 1

        for char in word2:
            if char not in freq_2:
                freq_2[char]=1
            freq_2[char] += 1
        

        return sorted(freq_1.values()) == sorted(freq_2.values()) 


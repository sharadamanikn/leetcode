class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict={}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num]=1
            else:
                freq_dict[num] += 1

        freq_arr=[ [] for _ in range(len(nums)+1) ]
        
        for n,f in freq_dict.items():
            freq_arr[f].append(n)
        
        res=[]

        for i in range(len(freq_arr)-1,0,-1):
            for n in freq_arr[i]:
                res.append(n)
                if len(res)==k:
                    return res


        
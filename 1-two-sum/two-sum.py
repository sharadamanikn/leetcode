class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_num_index={}

        for i,num in enumerate(nums):
            if target-num in seen_num_index:
                return [i,seen_num_index[target-num]]
            else:
                seen_num_index[num]=i
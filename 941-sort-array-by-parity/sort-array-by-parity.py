class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        ind=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[ind],nums[i]=nums[i],nums[ind]
                ind+=1
        return nums
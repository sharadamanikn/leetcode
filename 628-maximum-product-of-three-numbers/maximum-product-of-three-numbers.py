class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        m1=nums[n-1]*nums[n-2]*nums[n-3]
        m2=nums[0]*nums[1]*nums[n-1]
        return max(m1,m2)
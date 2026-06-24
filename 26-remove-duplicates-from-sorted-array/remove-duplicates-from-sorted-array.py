class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        idx=1
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[idx]=nums[i]
                idx+=1
        return idx
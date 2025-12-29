class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        r=[0]*n
        for i in range(len(nums)):
                r[(i+k)%n]=nums[i]
        for i in range(len(nums)):
            nums[i]=r[i]

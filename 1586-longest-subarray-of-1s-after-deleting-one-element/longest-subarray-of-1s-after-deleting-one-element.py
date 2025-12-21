class Solution(object):
    def longestSubarray(self, nums):
        left=0
        ans=0
        zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1
            ans=max(ans,i-left)
        return ans
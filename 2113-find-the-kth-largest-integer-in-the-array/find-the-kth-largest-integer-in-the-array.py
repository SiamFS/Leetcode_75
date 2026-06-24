class Solution(object):
    def kthLargestNumber(self, nums, k):
        lst=[]
        for i in nums:
            lst.append(int(i))
        sort=sorted(lst)
        return str(sort[-k])   
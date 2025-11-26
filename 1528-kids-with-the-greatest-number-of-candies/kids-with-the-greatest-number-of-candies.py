class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_n=max(candies)
        result=[]
        for i in range(len(candies)):
            candies[i]+=extraCandies
            if candies[i]>=max_n:
                result.append(True)
            else:
                result.append(False)
        return result
class Solution(object):
    def romanToInt(self, s):
            romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
            i=0
            sum=0
            while i<len(s):
                if i+1< len(s) and romanMap[s[i]]<romanMap[s[i+1]]:
                    sum+=romanMap[s[i+1]]-romanMap[s[i]]
                    i+=1
                else:
                    sum+=romanMap[s[i]]
                i+=1
            return sum
        

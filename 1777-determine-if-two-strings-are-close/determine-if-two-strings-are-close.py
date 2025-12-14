class Solution(object):
   def closeStrings(self, word1, word2):

    count1 = {}
    count2 = {}
    
    for c in word1:
        if c in count1:
            count1[c] += 1
        else:
            count1[c] = 1
    
    for c in word2:
        if c in count2:
            count2[c] += 1
        else:
            count2[c] = 1
    if set(count1.keys())!= set(count2.keys()):
        return False
    if sorted(count1.values()) != sorted(count2.values()):
        return False
    return True
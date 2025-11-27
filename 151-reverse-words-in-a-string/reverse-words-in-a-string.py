class Solution(object):
    def reverseWords(self, s):
        s = s.strip()  
        words = [w.strip() for w in s.split(" ") if w.strip()]
        words.reverse()
        return " ".join(words)
        

        
class Solution(object):
    def groupAnagrams(self, strs):
        dic = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord("a")] += 1

            dic[tuple(count)].append(i)

        return dic.values()
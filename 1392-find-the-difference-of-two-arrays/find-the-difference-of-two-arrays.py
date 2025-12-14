class Solution(object):
    def findDifference(self, nums1, nums2):

        def insert(arr, hash_map):
            for i in range(len(arr)):
                val = arr[i]
                if val not in hash_map:
                    hash_map[val] = 1
                else:
                    hash_map[val] += 1

        map1 = {}
        map2 = {}

        insert(nums1, map1)
        insert(nums2, map2)

        res1 = []
        res2 = []


        for key in map1:
            if key not in map2:
                res1.append(key)
        for key in map2:
            if key not in map1:
                res2.append(key)

        return [res1, res2]

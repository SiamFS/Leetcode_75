class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        i = 0
        length = len(flowerbed)

        while i < length:
            if flowerbed[i] == 1:
                i += 1
                continue
            start = i
            while i < length and flowerbed[i] == 0:
                i += 1
            end = i - 1

            zeros = end - start + 1
            if start == 0 and end == length - 1:
                count += (length + 1) // 2

            elif start == 0:
                count += zeros // 2
            elif end == length - 1:
                count += zeros // 2

            else:
                count += (zeros - 1) // 2

            if count >= n:
                return True

        return count >= n
        
# -*- coding: utf-8 -*- 
# __author__ = 'youzipi' 
#time:2015/9/12 10:49
class Solution:
    def findMaxDifference(self, arr, len):
        b = []
        for i in arr:
            b.append(i)
        m = max(arr)
        print "max=",m
        b = b[:b.index(m)]
        print "min=",min(b)
        if b == []:
            return 0
        else:
            return m - min(b)

s = Solution()
a = [10,5]
print s.findMaxDifference(a,2)
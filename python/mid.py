# -*- coding: utf-8 -*- 
# __author__ = 'youzipi' 
#time:2015/9/12 10:48
class Solution:
    def distance(self, s1, s2, len):
        print ord(s2[0]) - ord(s1[0])
        return 26*len*ord(s2[0]) - ord(s1[0])


s = Solution()
print s.distance("ab","ce",2)

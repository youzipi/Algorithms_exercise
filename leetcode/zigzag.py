"""
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(len(s) in [0,1,2]) or numRows <= 1:
            return s    
        rows = numRows
        size = 2*numRows-2
        s = [s[i*size:i*size+size] for i in range(int((len(s)-1)/size+1))]
        print(s)
        result = ''
        for index in range(rows): 
            for g_index in range(len(s)):
                result += s[g_index][index:index+1]
                if(index not in [0,rows-1]):
                    result += s[g_index][size-index:size-index+1]
        return result
        
s = Solution()
print(s.convert('ABC',2))
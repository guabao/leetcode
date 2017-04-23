class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        column = 0
        for ch in s:
            column = column * 26 + ord(ch) - ord('A') + 1
        return column
        

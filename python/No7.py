class Solution:
    # @return an integer
    def reverse(self, x):
        if x<0:
            x = -x
            symbol = -1
        else:
            symbol = 1
        new = 0
        while x != 0:
            x, mod = divmod(x, 10)
            new = new * 10 + mod
        if new > 2147483647:
            new = 0
        new = new * symbol
        return new
            

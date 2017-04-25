class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
             ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
             ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
             ["","M","MM","MMM","MMMM"]]
             
             
        return d[3][num / 1000] + d[2][(num % 1000) / 100] + d[1][(num % 100) / 10] + d[0][num % 10]

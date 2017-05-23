class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':['a','b','c'], '3':['d','e', 'f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '0':[' '], '1': ['*']}
        
        l = []
        
        if not digits:
            return []
        
        for di in digits:
            l += [d[di]]
        
        return map("".join, list(itertools.product(*l)))

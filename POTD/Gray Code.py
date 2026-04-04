class Solution:
    def graycode(self, n):
        if n == 0:
            return ["0"]
        
        res = ["0", "1"]
        
        for i in range(2, n + 1):
            nlist = []
            for code in res:
                nlist.append("0" + code)
            for code in reversed(res):
                nlist.append("1" + code)
            res = nlist
        return res
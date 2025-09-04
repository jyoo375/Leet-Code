class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d=[]
        g=''
        for i in digits:
            g+=str(i)
        k=int(g)
        h=str(k+1)
        for i in h:
            d.append(int(i))
        return d


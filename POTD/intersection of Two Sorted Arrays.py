class Solution:
    def intersection(self,a, b):
        s1,s2 = set(a),set(b)
        s3 = s1.intersection(s2)
        return sorted(list(s3))
        
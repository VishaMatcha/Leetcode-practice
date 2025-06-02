class Solution:
    def candy(self, a: List[int]) -> int:
        f = lambda a:[*accumulate(map(lt,a,a[1:]),lambda q,p:q*p+1,initial=1)]
        return sum(map(max,f(a),f(a[::-1])[::-1]))
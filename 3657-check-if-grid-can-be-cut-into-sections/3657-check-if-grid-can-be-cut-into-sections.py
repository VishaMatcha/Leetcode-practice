class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def cut3(i):
            rectangles.sort(key=itemgetter(i))
            b, cnt=rectangles[0][i+2], 0
            for r in rectangles[1:]:
                c=r[i]
                d=r[i+2]
                if c<b:
                    b=max(b, d)
                else:
                    cnt+=1
                    b=d
                if cnt>=2: return True
            return False
        return cut3(0) or cut3(1)
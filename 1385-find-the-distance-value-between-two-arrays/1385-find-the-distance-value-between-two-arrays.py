class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        m = len(arr2)
        ans = 0
        
        for x in arr1:
            idx = bisect_left(arr2, x - d)
            if idx < m and abs(arr2[idx] - x) <= d:
                continue
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                continue
            ans += 1
            
        return ans